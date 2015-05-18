import scrapy

from iitnews.items import IitNewsItem
from iitnews.constants import iit_list

class ToiSpider(scrapy.Spider):
  name ="toi"
  allowed_domains = ["timesofindia.indiatimes.com"]
  def start_requests(self):
    for iit in iit_list:
      for i in range(1,10):
        yield self.make_requests_from_url("http://timesofindia.indiatimes.com/topic/%s/%s/" % (iit,i) )
  
  def parse(self, response):
    news_page_no = int(response.url.split("/")[5])
    news_college = response.url.split("/")[4]
    news_latest = response.xpath('//div[@id="tab-news-any"]')
    news_list = news_latest.xpath('.//div[@class="topicsnews-box clearfix"]')
    for news in news_list:
      news_headline = news.xpath('.//strong/text()').extract()
      news_synopsis = news.xpath('.//span[@class="topicnews-synopsis"]/text()').extract()
      news_link = news.xpath('.//a/@href').extract()
      item = IitNewsItem()
      item['headline'] = news_headline[0]
      if not news_synopsis:
        item['synopsis'] = "No synopsis"
      else:
        item['synopsis'] = news_synopsis[0]
      item['link'] = 'http://timesofindia.indiatimes.com' + news_link[0]
      item['page_no'] = news_page_no
      item['college'] = news_college
      yield item
