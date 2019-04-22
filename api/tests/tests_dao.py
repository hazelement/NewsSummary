from datetime import datetime, timedelta


from django.test import TestCase

from api.dao import SiteDao, UrlDigestionDao, DailyDigestionDao, UrlDigestionAPIModel


class SiteDaoTest(TestCase):

    def test_add_site(self):
        test_site_name = "test"
        test_site_url = "https://test url"
        site = SiteDao().add_site(test_site_name, test_site_url)

        assert SiteDao().get_site(test_site_url) is not None


class UrlDigestionDaoTest(TestCase):

    def test_add_entry(self):
        url_digestion = UrlDigestionAPIModel("https://test.com", None, None, "test", "test digestion")
        UrlDigestionDao().set_entry(url_digestion.url, url_digestion)
        assert UrlDigestionDao().get_entry(url_digestion.url)


class DailyDigestionDaoTest(TestCase):

    def test_add_digestion(self):
        test_site_name = "test"
        test_site_url = "https://test url"
        site = SiteDao().add_site(test_site_name, test_site_url)

        url_digestion = UrlDigestionAPIModel("https://test.com", None, None, "test", "test digestion")
        UrlDigestionDao().set_entry(url_digestion.url, url_digestion)

        DailyDigestionDao().add_digestion(site, UrlDigestionDao().get_entry(url_digestion.url))

        start_time = datetime.utcnow() - timedelta(days=1)

        assert len(DailyDigestionDao().get_digestion(site, start_time)) > 0
