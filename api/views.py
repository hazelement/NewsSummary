from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse

import json
from newspaper import Article

from api.article_handler import ArticleDigestion
# Create your views here.
class RESTfulView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)


class ArticleView(RESTfulView):

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))

        url = data['url']

        article_digestion = ArticleDigestion(url)

        return HttpResponse(article_digestion.get_summary())