## About

This project aims to provide an end point on top of newpaper3k for user to summarize news articles. It also have a home page that shows summarized news from major news sites. 

## Todo

- [x] implement based on uml design
- [x] scrape engine to create article entry in database daily from popular news sites
- [x] webpage that list latest article summary from popular news sites
- [ ] schedule jobs to run periodically to scrape news sites, use Celery
- [ ] reddit bot
- [ ] twitter bot

### Features

1. Caching in redis and db
2. Content based summary API end point rather than url
3. Plugins, chrome, safari that talks to this end point.
