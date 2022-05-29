import random
from sqlite3 import DatabaseError
from typing import Any

from django import db
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from ex.forms import *
from ex.models import TipModel


from d06.settings import DEFAULT_NAMES
from random import randint

is_login = False

class Index(View):
    template_name = "index.html"

    def get(self, request):
        try:
            tips = TipModel.objects.all().order_by('-date')
        except db.DatabaseError as e:
            tips = []
        if not is_login and 'name' not in request.session:
            request.session.set_expiry(42)
            request.session['name'] = DEFAULT_NAMES[randint(0, 9)]
        context = {
            'tipform': TipForm(),
            'tips': [{
                'id': tip.id,
                'content': tip.content,
                'author': tip.author,
                'date': tip.date,
                'up_votes': tip.up_votes,
                'down_votes': tip.down_votes,
                'deleteform': DeleteTipForm(tip.id),
                'voteform': VoteForm(tip.id),
            } for tip in tips],
            'new_name': request.session['name']
        }
        return render(request, self.template_name, context)


class Register(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('index')
    my_request = None

    def get_name(self):
        if not self.my_request.user.is_authenticated and 'name' not in self.my_request.session:
            self.my_request.session.set_expiry(42)
            self.my_request.session['name'] = DEFAULT_NAMES[randint(0, 9)]
        return self.my_request.session['name']

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['new_name'] = self.get_name()
        return context

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.my_request = request
        if self.request.user.is_authenticated:
            messages.error(self.request, 'You already logined!')
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: RegisterForm):
        user = form.save()
        login(self.request, user)
        is_login = True
        messages.success(self.request, "Registration successful.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Unsuccessful registration. Invalid information.")
        return super().form_invalid(form)


class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    my_request = None

    def get_name(self):
        if not self.my_request.user.is_authenticated and 'name' not in self.my_request.session:
            self.my_request.session.set_expiry(42)
            self.my_request.session['name'] = DEFAULT_NAMES[randint(0, 9)]
        return self.my_request.session['name']

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['new_name'] = self.get_name()
        return context

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.my_request = request
        if self.request.user.is_authenticated:
            messages.error(self.request, 'You already logined!')
            return redirect('index')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: AuthenticationForm):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            messages.error(self.request, "Invalid username or password.")
            return
        login(self.request, user)
        is_login = True
        messages.info(self.request, f"You are now logged in as {username}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class Logout(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        logout(request)
        is_login = False
        messages.info(request, "You have successfully logged out.")
        return redirect('index')


class Profile(LoginRequiredMixin, View):
    template_name = "profile.html"
    login_url = reverse_lazy('login')

    def get(self, request):
        try:
            tips = TipModel.objects.filter(
                author=request.user).order_by('-date')

        except db.DatabaseError as e:
            tips = []
        context = {
            'tipform': TipForm(),
            'tips': [{
                'id': tip.id,
                'content': tip.content,
                'author': tip.author,
                'date': tip.date,
                'up_votes': tip.up_votes,
                'down_votes': tip.down_votes,
                'deleteform': DeleteTipForm(tip.id),
                'voteform': VoteForm(tip.id),
            } for tip in tips],
        }
        print([(tip.up_votes.count(), tip.down_votes.count()) for tip in tips])
        return render(request, self.template_name, context)


class Tip(LoginRequiredMixin, View):
    http_method_names = ['post', 'put', 'delete']
    login_url = reverse_lazy('login')

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(Tip, self).dispatch(*args, **kwargs)

    def post(self, request):
        form = TipForm(request.POST)
        if form.is_valid():
            try:
                TipModel.objects.create(
                    content=form.cleaned_data['content'],
                    author=self.request.user
                )
                messages.success(self.request, "Successful create Tip.")
            except DatabaseError as e:
                print(e)
                messages.error(
                    self.request, "Unsuccessful create Tip. (db error)")
        else:
            messages.error(
                self.request, "Unsuccessful create Tip. (Invalid form data.)")
        return redirect('index')

    def __error_msg(self, method, msg):
        messages.error(
            self.request, f"Unsuccessful {method} Tip. ({msg})")
        return redirect('index')

    def delete(self, request: HttpRequest):
        form = DeleteTipForm(None, request.POST)
        if not form.is_valid():
            return self.__error_msg("delete", "Invaild form data.")
        try:
            tip: TipModel = TipModel.objects.get(
                id=form.cleaned_data['id'])
            if tip.author != request.user and request.user.is_staff == False and request.user.is_superuser == False:
                return self.__error_msg("delete", "access denied")
            tip.delete()
            messages.success(self.request, "Successful delete Tip.")
        except TipModel.DoesNotExist as e:
            return self.__error_msg("delete", "Tip does not exist")
        except DatabaseError as e:
            return self.__error_msg("delete", "db error")

        return redirect('index')

    def put(self, request):
        form = VoteForm(None, request.POST)
        if not form.is_valid():
            return self.__error_msg("vote", "Invaild form data.")
        try:
            tip: TipModel = TipModel.objects.get(id=form.cleaned_data['id'])
            if form.cleaned_data['type']:
                tip.upvote(request.user)
            elif tip.author != request.user and request.user.groups.filter(name='blacklist').exists():
                return self.__error_msg("vote", "you can't do that!!")
            else:
                tip.downvote(request.user)
        except TipModel.DoesNotExist as e:
            return self.__error_msg("vote", "Tip does not exist")
        except DatabaseError as e:
            return self.__error_msg("vote", "db error")
        messages.success(request, 'Voted success!')
        return redirect('index')