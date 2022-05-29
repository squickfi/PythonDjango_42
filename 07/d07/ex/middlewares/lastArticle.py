from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin

from ex.forms import LoginForm
from ex.models import Article


class LastArticleMiddlware(MiddlewareMixin):
    def process_template_response(self, request: HttpRequest, response: HttpResponse):
        articles = Article.objects.all().order_by('-id')
        if len(articles):
            response.context_data["last_article"] = articles[0]
        response.context_data['login_form'] = LoginForm
        return response
