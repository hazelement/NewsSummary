from django.test import TestCase
from api.article_handler import ArticleDigestion

class ArticleTest(TestCase):
    def setUp(self):
        url = "https://www.cbc.ca/news/politics/mint-coin-loonie-homosexual-rights-1.5095317"
        self.article = ArticleDigestion(url)

    def test_summary(self):
        print(self.article.get_summary())