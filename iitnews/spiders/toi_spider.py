import scrapy

from iitnews.items import IitNewsItem

class ToiSpider(scrapy.Spider):
  name ="toi"
  allowed_domains = ["timesofindia.indiatimes.com"]
  start_urls = [
    "http://timesofindia.indiatimes.com/topic/IIT-Bombay"
  ]
  def parse(self, response):
    filename = "toi_" + response.url.split("/")[-1]
    with open(filename, 'wb') as f:
      f.write(response.body)

