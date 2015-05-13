# iit-news-python-scraper
A Scrapy-based news crawler of different IIT's from Times of India.

## Introduction
A Scrapy-based crawler that crawls the Times of India website and returns the news related to different IIT's in JSON format.The results are segregated for different IIT's and ordered by datetime.

## Dependencies
- Scrapy

## Installation
```sh
$ pip install scrapy
$ git clone git@github.com:namit9/iit-news-python-scraper.git
$ cd iit-news-python-scraper
$ python update_news.py
```

## Output
The results are stored in toi_organised.json.
Each news item looks like this:
```sh
 {
 headline: "Pune's Sourav Pal invited by IIT-K to be a 'distinguished visiting professor'",
 link: "/city/pune/Punes-Sourav-Pal-invited-by-IIT-K-to-be-a-distinguished-visiting-professor/articleshow/46897750.cms",
 synopsis: "Sourav Pal, director CSIR- National Chemical Laboratory, Pune has been invited to be a ‘Distinguished  Visiting Professor’ at Indian Institute of Technology (IIT), Kharagpur for the period of five years.",
 college: "IIT-Kharagpur",
 page_no: 1
 }
```
