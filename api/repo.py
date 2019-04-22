
from abc import ABC, abstractmethod
from api.models import UrlDigestionDBModel
from singleton_decorator import singleton
import redis
import fakeredis

from article_summary.settings import REDIS_HOST, REDIS_PORT, TESTING
from api.api_models import UrlDigestionAPIModel
from api.lib.article_handler import UrlDigestion

class UrlAccessInterface(ABC):

    @abstractmethod
    def get_entry(self, url):
        """ returns UrlDigestionAPIModel """
        return

    @abstractmethod
    def set_entry(self, url, url_digestion_api_model):
        """ save url digestion """
        return


@singleton
class UrlDigestionDao(UrlAccessInterface):

    def get_entry(self, url):
        db_url = UrlDigestionDBModel.objects.filter(url=url).first()
        if db_url is not None:
            return UrlDigestionAPIModel(url,
                                        db_url.publish_date,
                                        db_url.author,
                                        db_url.title,
                                        db_url.digestion)
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
class UrlDigestionRedis(UrlAccessInterface):

    def __init__(self):
        if TESTING:
            self.r = fakeredis.FakeStrictRedis()
        else:
            self.r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def get_entry(self, url):
        digestion = self.r.get(url+"digestion")
        author = self.r.get(url + "author")
        title = self.r.get(url + "title")
        publish_date = self.r.get(url + "publish_date")

        if digestion is not None:
            return UrlDigestionAPIModel(url=url,
                                        publish_date=publish_date,
                                        author=author,
                                        title=title,
                                        digestion=digestion)
        else:
            return None

    def set_entry(self, url, digestion):
        assert isinstance(digestion, UrlDigestionAPIModel)
        self.r.set(url+"digestion", digestion.digestion)
        self.r.set(url + "author", digestion.author)
        self.r.set(url + "title", digestion.title)
        self.r.set(url + "publish_date", digestion.publish_date)


@singleton
class DigestionRepo(object):

    def get_digestion(self, url):
        """

        :param url:
        :return: UrlDigestionAPIModel
        """

        # retrieve from redis cache
        cache_digestion = UrlDigestionRedis().get_entry(url)
        if cache_digestion:
            return cache_digestion

        # retrieve from DB
        db_digestion = UrlDigestionDao().get_entry(url)
        if db_digestion:
            UrlDigestionRedis().set_entry(url, db_digestion)
            return db_digestion

        # perform new digestion
        article_digestion = UrlDigestion(url).get_digestion()

        UrlDigestionDao().set_entry(url, article_digestion)
        UrlDigestionRedis().set_entry(url, article_digestion)
        return article_digestion
