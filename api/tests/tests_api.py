from django.test import TestCase
import json


class BaseTest(TestCase):
    """
    Base test class the provide all url variables and API call methods
    """
    article_url = '/api/v1.0/article'


    def test_article_summary(self):
        d = {
                'url': "https://www.cbc.ca/news/politics/mint-coin-loonie-homosexual-rights-1.5095317",
            }
        response = self.client.put(self.article_url, data=d, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        assert "url" in data
        assert 'publish_date' in data
        assert 'author' in data
        assert 'title' in data
        assert 'digestion' in data