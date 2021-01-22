import scrapy


class GetKvSpider(scrapy.Spider):
    name = 'get_kv'
    allowed_domains = ['no1bhubaneswar.kvs.ac.in','no2bhubaneswar.kvs.ac.in','no3bhubaneswar.kvs.ac.in','no4bhubaneswar.kvs.ac.in','no5bhubaneswar.kvs.ac.in','no6bhubaneswar.kvs.ac.in']
    start_urls = ['https://no1bhubaneswar.kvs.ac.in/','https://no2bhubaneswar.kvs.ac.in/','https://no3bhubaneswar.kvs.ac.in/','https://no4bhubaneswar.kvs.ac.in/','https://no5bhubaneswar.kvs.ac.in/','https://no6bhubaneswar.kvs.ac.in/']

    def parse(self, response):
        all_data = response.css("html").extract_first()
        # print(str(response))
        f = open("scraped_data/"+str(response).split("https://")[-1].split("/>")[0]+".html","w")
        f.write(all_data)
        f.close()