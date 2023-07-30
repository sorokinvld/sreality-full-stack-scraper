from scrapy.crawler import CrawlerProcess
from srealitySpider import SrealitySpider

process = CrawlerProcess(settings={
    "FEEDS": {
        "out.json": {"format": "json"},
    },
})
process.crawl(SrealitySpider)
process.start()