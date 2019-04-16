from newspaper import Article


class ArticleDigestion(object):

    def __init__(self, url):

        # todo setup caching db and redis
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        self.article = article

    def get_summary(self):
        return self.article.summary
