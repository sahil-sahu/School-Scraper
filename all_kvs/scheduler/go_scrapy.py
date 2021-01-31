from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')


def startit():
    data = ['https://no1bhubaneswar.kvs.ac.in/', 'https://no2bhubaneswar.kvs.ac.in/', 'https://no3bhubaneswar.kvs.ac.in/',
                  'https://no4bhubaneswar.kvs.ac.in/', 'https://no5bhubaneswar.kvs.ac.in/', 'https://no6bhubaneswar.kvs.ac.in/']
    print("going for scrapy")
    task = scrapyd.schedule('school_scraper', 'get_kv', links = '\n'.join(data))

def updateit():
    data = ["bala",]
    task = scrapyd.schedule('school_scraper', 'get_kv', links = data)    
    