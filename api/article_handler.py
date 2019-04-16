from newspaper import Article


class ArticleDigestion(object):

    def __init__(self, url):

        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        self.article = article

    def get_summary(self):
        return self.article.summary
