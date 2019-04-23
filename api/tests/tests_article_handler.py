from django.test import TestCase
from api.src.article_handler import UrlSummary

class ArticleTest(TestCase):
    def setUp(self):
        url = "https://www.cbc.ca/news/politics/mint-coin-loonie-homosexual-rights-1.5095317"
        self.article = UrlSummary(url)

    def test_summary(self):
        print(self.article.get_digestion())