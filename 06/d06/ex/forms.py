import django.contrib.auth.forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import HiddenInput


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",  "password1", "password2")


class LogInForm(AuthenticationForm):
    model = User
    fields = ("username", "password1")


class TipForm(forms.Form):
    content = forms.CharField(required=True)


class DeleteTipForm(forms.Form):
    _method = forms.CharField(widget=HiddenInput(), initial='delete')
    id = forms.IntegerField(widget=HiddenInput())

    def __init__(self, id, *args, **kwargs):
        super(DeleteTipForm, self).__init__(*args, **kwargs)
        if id:
            self.fields['id'].initial = id


class VoteForm(forms.Form):
    _method = forms.CharField(widget=HiddenInput(), initial='put')
    id = forms.IntegerField(widget=HiddenInput())
    type = forms.BooleanField(required=False)

    def __init__(self, id, *args, **kwargs):
        super(VoteForm, self).__init__(auto_id='%s', *args, **kwargs)
        if id:
            self.fields['id'].initial = id