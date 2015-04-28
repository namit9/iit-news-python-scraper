import subprocess
import json

iit_list = ["IIT-Bombay", "IIT-Roorkee", "IIT-Guwahati", "IIT-Kanpur", "IIT-Kharagpur", "IIT-Madras", "IT-BHU", "IIT-Delhi"]

if subprocess.call(["rm", "toi.json"]) == 0:
  if subprocess.call("scrapy crawl toi -o toi.json", shell = True) == 0:
    with open("toi.json", "r") as f:
      news_list = json.load(f)
    news_segregated = {}
    news_ordered = {}
    for iit in iit_list:
      news_segregated[iit] = [news for news in news_list if news['college'] == iit]
      news_ordered[iit] = sorted(news_segregated[iit], key=lambda news:news['page_no'])
    with open("toi_organised.json", "w") as f:
      json.dump(news_ordered, f)
