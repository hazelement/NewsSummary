from singleton_decorator import singleton
import redis
import fakeredis

from api.interfaces import UrlDigestionInterface
from article_summary.settings import REDIS_HOST, REDIS_PORT, TESTING
from api.api_models import UrlDigestionAPIModel
from api.lib.article_handler import UrlSummary


@singleton
class UrlDigestionRedis(UrlDigestionInterface):

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


from api.dao import UrlDigestionDao
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
            digestion = UrlDigestionAPIModel.from_db_model(db_digestion)
            UrlDigestionRedis().set_entry(url, digestion)
            return digestion

        # perform new digestion
        article_digestion = UrlSummary(url).get_digestion()

        UrlDigestionDao().set_entry(url, article_digestion)
        UrlDigestionRedis().set_entry(url, article_digestion)
        return article_digestion
