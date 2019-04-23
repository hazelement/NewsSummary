from newspaper import Article
from api.api_models import UrlDigestionAPIModel


class UrlSummary(object):

    def __init__(self, url):
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        self.article = article

    def get_digestion(self):
        if len(self.article.summary) < 10:
            raise Exception("Unable to generate summary")
        return UrlDigestionAPIModel(self.article.url,
                                    self.article.publish_date,
                                    ", ".join(self.article.authors),
                                    self.article.title,
                                    self.article.summary)
