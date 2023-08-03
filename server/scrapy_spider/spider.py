from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from .srealitySpider.spiders import sreality
# from srealitySpider.pipelines import PostgresPipeline

def run_spider():
  s = get_project_settings()
  # s.update({
  #   'ITEM_PIPELINES': {
  #     # pipelines.PostgresPipeline: 300
  #   }
  # })
  print(list(s["ITEM_PIPELINES"]))

  process = CrawlerProcess(s)
  process.crawl(sreality.SrealitySpider)
  process.start()