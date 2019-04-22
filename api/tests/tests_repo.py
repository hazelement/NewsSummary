from django.test import TestCase
from api.repo import UrlDigestionDao, UrlDigestionRedis, DigestionRepo


class BaseTest(TestCase):

    def test_summary(self):
        url= "https://www.cbc.ca/news/politics/mint-coin-loonie-homosexual-rights-1.5095317"

        t = DigestionRepo().get_digestion(url)

        assert t is not None
        assert UrlDigestionDao().get_entry(url) is not None
        assert UrlDigestionRedis().get_entry(url) is not None
