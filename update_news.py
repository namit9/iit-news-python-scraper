import subprocess
import json
import os.path
import collections

from iitnews.constants import iit_list

if os.path.isfile("toi.json") == True:
  subprocess.call(["rm", "toi.json"])

if subprocess.call("scrapy crawl toi -o toi.json", shell = True) == 0:
  with open("toi.json", "r") as f:
    news_list = json.load(f)
  news_segregated = {}
  news_ordered = {}
  for iit in iit_list:
    news_segregated[iit] = [news for news in news_list if news['college'] == iit]
    news_ordered[iit] = sorted(news_segregated[iit], key=lambda news:news['page_no'])
    news_ordered = collections.OrderedDict(sorted(news_ordered.items()))
  with open("toi_organised.json", "w") as f:
    json.dump(news_ordered, f)
