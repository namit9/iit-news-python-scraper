# iit-news-python-scraper
A Scrapy-based news crawler of different IIT's from Times of India.

## Introduction
A Scrapy-based crawler that crawls the Times of India website and returns the news related to different IIT's in JSON format.The results are segregated for different IIT's and ordered by datetime.

## Dependencies
- Scrapy
- Django(for demo project)

## Installation
```sh
$ pip install scrapy
$ git clone git@github.com:namit9/iit-news-python-scraper.git
$ cd iit-news-python-scraper
$ python update_news.py
$ ./manage.py runserver(to see result in the browser)
```

## Output
### API
- localhost:8000/api/?items=:items&iit=IIT-Bombay&iit=IIT-Delhi&...
  - items=number of news items for each IIT
  - To get news for all IITs, remove "iit" parameter from URL 

Each news item looks like this:
```sh
 {
 headline: "Pune's Sourav Pal invited by IIT-K to be a 'distinguished visiting professor'",
 link: "http://timesofindia.indiatimes.com/city/pune/Punes-Sourav-Pal-invited-by-IIT-K-to-be-a-distinguished-visiting-professor/articleshow/46897750.cms",
 synopsis: "Sourav Pal, director CSIR- National Chemical Laboratory, Pune has been invited to be a ‘Distinguished  Visiting Professor’ at Indian Institute of Technology (IIT), Kharagpur for the period of five years.",
 college: "IIT-Kharagpur",
 page_no: 1
 }
```
