
from abc import ABC, abstractmethod
from datetime import datetime


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

    def serialize(self):
        return {"url":  self.url,
                "publish_date": self.publish_date,
                "author": self.author,
                "title": self.title,
                "digestion": self.digestion}

