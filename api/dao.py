from datetime import datetime

from singleton_decorator import singleton

from api.api_models import UrlDigestionAPIModel
from api.models import UrlDigestionDBModel, Site, DailyDigestion
from api.interfaces import UrlDigestionInterface


@singleton
class UrlDigestionDao(UrlDigestionInterface):

    def get_entry(self, url):
        """
        get entry
        :param url:
        :return: UrlDigestionDBModel
        """
        db_url = UrlDigestionDBModel.objects.filter(url=url).first()
        if db_url is not None:
            return db_url
        else:
            return None

    def set_entry(self, url, digestion):
        assert isinstance(digestion, UrlDigestionAPIModel)
        db_url = UrlDigestionDBModel(url=digestion.url,
                                     digestion=digestion.digestion,
                                     author=digestion.author,
                                     title=digestion.title,
                                     publish_date=digestion.publish_date)
        db_url.save()
        return db_url is not None


@singleton
class SiteDao(object):

    def add_site(self, site_name, site_url):
        # todo add site url format check and clean up
        site = Site(name=site_name, url=site_url)
        site.save()
        return site

    def get_site(self, site_url):
        site = Site.objects.filter(url=site_url).first()
        return site


@singleton
class DailyDigestionDao(object):

    def add_digestion(self, site, url_digestion):
        assert isinstance(site, Site)
        assert isinstance(url_digestion, UrlDigestionDBModel)

        daily_digestion = DailyDigestion(site=site,
                                         url_digestion=url_digestion)
        daily_digestion.save()
        return daily_digestion

    def get_digestion(self, site, gt_time):
        """
        get digestion for a specific site
        :param site: site to get digestion for
        :param gt_time: get digestion created greater than a time
        :return: list of UrlDigestionDBModel
        """
        assert isinstance(site, Site)
        assert isinstance(gt_time, datetime)
        daily_digestions = DailyDigestion.objects.filter(site=site).filter(created__gte=gt_time).all()
        return [digestion.url_digestion for digestion in daily_digestions]
