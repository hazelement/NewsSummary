from django.conf.urls import url

from api.views import ArticleView

urlpatterns = [
    url(r'^v1.0/article', ArticleView.as_view()),
]