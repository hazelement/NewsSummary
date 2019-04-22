from abc import ABC, abstractmethod


class UrlDigestionInterface(ABC):

    @abstractmethod
    def get_entry(self, url):
        """ returns UrlDigestionAPIModel """
        return

    @abstractmethod
    def set_entry(self, url, url_digestion_api_model):
        """ save url digestion """
        return