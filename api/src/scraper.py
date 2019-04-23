

import newspaper
from api.src.article_handler import UrlSummary
from api.dao import SiteDao, UrlDigestionDao, DailyDigestionDao


class Scraper(object):

    def scrape(self):
        sites = newspaper.popular_urls()
        for site in sites[0:10]:
            try:
                # process each site
                print(f"Processing site {site}")
                site_info = newspaper.build(site, memoize_articles=False)
                saved_site = SiteDao().get_site(site)
                if not saved_site:
                    print(f"Creating new site entry for {site}")
                    saved_site = SiteDao().add_site(site_info.brand, site)

                # process each article
                for item in site_info.articles[0:10]:
                    try:
                        url = item.url
                        print(f"Processing article {url}")
                        url_digestion = UrlDigestionDao().get_entry(url)
                        if not url_digestion:
                            print(f"Creating new digestion entry for {url}")
                            url_digestion = UrlSummary(url).get_digestion()
                            UrlDigestionDao().set_entry(url, url_digestion)
                            url_digestion = UrlDigestionDao().get_entry(url)

                        print(f"Creating new daily entry for {site} and {url}")
                        DailyDigestionDao().add_digestion(saved_site, url_digestion)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
