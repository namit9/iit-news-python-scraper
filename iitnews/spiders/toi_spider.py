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
    news_list = response.xpath('//div[@class="topicsnews-box clearfix"]')
    for news in news_list:
      news_headline = news.xpath('.//strong/text()').extract()
      news_synopsis = news.xpath('.//span[@class="topicnews-synopsis"]/text()').extract()
      news_link = news.xpath('.//a/@href').extract()
      news_item = {
        'headline':news_headline[0],
        'synopsis':news_synopsis[0], 
        'link':news_link[0]
      }
      item = IitNewsItem()
      item['headline'] = news_headline[0]
      item['synopsis'] = news_synopsis[0]
      item['link'] = news_link[0]
      yield item
