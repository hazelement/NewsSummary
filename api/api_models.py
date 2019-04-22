
from abc import ABC, abstractmethod
from datetime import datetime
from api.models import UrlDigestionDBModel

class Serializable(ABC):

    @abstractmethod
    def serialize(self):
        return


class UrlDigestionAPIModel(Serializable):

    def __init__(self, url, publish_date, author, title, digestion):
        assert isinstance(url, str)
        if publish_date is None:
            publish_date = ""
        if author is None:
            author = ""
        if title is None:
            title = ""
        if digestion is None:
            digestion = ""

        self.url = url
        self.publish_date = publish_date
        self.author = author
        self.title = title
        self.digestion = digestion

    @classmethod
    def from_db_model(cls, url_digestion_db_model):
        assert isinstance(url_digestion_db_model, UrlDigestionDBModel)
        return UrlDigestionAPIModel(url_digestion_db_model.url,
                                    url_digestion_db_model.publish_date,
                                    url_digestion_db_model.author,
                                    url_digestion_db_model.title,
                                    url_digestion_db_model.digestion)

    def serialize(self):
        return {"url":  self.url,
                "publish_date": self.publish_date,
                "author": self.author,
                "title": self.title,
                "digestion": self.digestion}

