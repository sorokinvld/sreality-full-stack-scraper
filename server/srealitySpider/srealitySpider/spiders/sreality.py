import json
import scrapy
from ..items import FlatItem


class SrealitySpider(scrapy.Spider):
    name = "sreality"
    allowed_domains = ["www.sreality.cz"]
    start_urls = ["https://www.sreality.cz/api/en/v2/estates?category_main_cb=&category_type_cb=1&per_page=500&tms=1690675338262"]

    def parse(self, response):
        data = json.loads(response.body)
        for estate in data["_embedded"]["estates"]:
            flat_item = FlatItem()
            flat_item["title"] = estate["name"]
            flat_item["image_url"] = estate["_links"]["images"][0]["href"]
            
            yield flat_item    