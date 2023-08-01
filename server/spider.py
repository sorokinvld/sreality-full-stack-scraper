from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from srealitySpider.srealitySpider.spiders import SrealitySpider

process = CrawlerProcess(get_project_settings())
process.crawl(SrealitySpider)
process.start()