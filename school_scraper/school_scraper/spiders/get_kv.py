import scrapy


class GetKvSpider(scrapy.Spider):
    name = 'get_kv'
    allowed_domains = ['no3bhubaneswar.kvs.ac.in']
    start_urls = ['https://no3bhubaneswar.kvs.ac.in/']

    def parse(self, response):
        print("bala")
