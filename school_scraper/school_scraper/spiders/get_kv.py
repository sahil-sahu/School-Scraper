import scrapy


class GetKvSpider(scrapy.Spider):
    name = 'get_kv'
    allowed_domains = ['no3bhubaneswar.kvs.ac.in']
    start_urls = ['https://no3bhubaneswar.kvs.ac.in/']

    def parse(self, response):
        all_data = response.css("html").extract_first()
        f = open("../scraped_data/data.html","w")
        f.write(all_data)
        f.close()