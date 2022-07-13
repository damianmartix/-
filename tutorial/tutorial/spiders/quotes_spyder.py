import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["wikipedia.org"]
    start_urls = ['https://en.wikipedia.org/wiki/Excavator_(microarchitecture)']

    #custom_settings = {
        #'SPLASH_USER': 'splash-user',
        #'SPLASH_PASS': 'splash-password',
    #}

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            yield SplashRequest(
                link.url,
                self.parse_link,
                endpoint='render.json',
                args={
                    'har': 1,
                    'html': 1,
                }
            )

    def parse_link(self, response):
        print("PARSED", response.real_url, response.url)
        print(response.css("title").extract())
        print(response.data["har"]["log"]["pages"])
        print(response.headers.get('Content-Type'))


