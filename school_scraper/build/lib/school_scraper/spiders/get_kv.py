import scrapy
from scrapy.utils.response import open_in_browser
import os

class GetKvSpider(scrapy.Spider):
    name = 'get_kv'
    # allowed_domains = ['no1bhubaneswar.kvs.ac.in','no2bhubaneswar.kvs.ac.in','no3bhubaneswar.kvs.ac.in','no4bhubaneswar.kvs.ac.in','no5bhubaneswar.kvs.ac.in','no6bhubaneswar.kvs.ac.in']
    start_urls = ['https://no1bhubaneswar.kvs.ac.in/','https://no2bhubaneswar.kvs.ac.in/','https://no3bhubaneswar.kvs.ac.in/','https://no4bhubaneswar.kvs.ac.in/','https://no5bhubaneswar.kvs.ac.in/','https://no6bhubaneswar.kvs.ac.in/']
    # start_urls = ['https://no1bhubaneswar.kvs.ac.in/']
    a_tags = []

    def parse(self, response):
        all_data = response.css("html").extract_first()
        all_tags = response.css("a")
        
        # print(a_tags,sep='\n')
        BASE_DIR = "../scraped_data/"
        path = os.path.join(BASE_DIR,str(response).split("https://")[-1].split("/>")[0]) 
        if not(os.path.isdir(path))  :
            os.mkdir(path)
        for i in all_tags:
            temp = i.xpath("@href").extract_first()
            # print(i.xpath("@href").extract_first())
            try:
                if "http" not in temp and len(temp.split('/')[1::]) > 0 and [''] != temp.split('/')[1::]:
                    dirs = list(temp.split('/')[1::])
                    self.a_tags.append(dirs)
                    self.makedir(path,dirs)
            except:
                pass    
            # i['href'].extract_fist() += "Bala"
            # print(i['href'].extract_fist())
        # f = open("scraped_data/"+str(response).split("https://")[-1].split("/>")[0]+".html","w")
        f = open(path+"/index.html","w")
        # f = open("index.html","w")
        x = all_data.replace('href="/', 'href="./')
        y = x.replace('src="/', 'src="'+response.url+'/')
        f.write(y)
        f.close()
        for i in self.a_tags:
            yield response.follow("/".join(i), callback=self.temp)
    
    def temp(self,response):
        baseurl = response.url.split("kvs.ac.in/")[0]+"kvs.ac.in"
        BASE_DIR = "../scraped_data/"
        path = os.path.join(BASE_DIR,response.url.split("https://")[1]) 
        # os.mkdir(path)
        # print(path,type(path))
        f = open(path+"/index.html","w")
        all_data = response.css("html").extract_first()
        
        x = all_data.replace('href="/', 'href="'+response.url.split("https://")[1].count('/')*'../')
        y = x.replace('src="/', 'src="'+baseurl+"/")
        f.write(y)
        f.close() 
        # yield {1:baseurl}
    def makedir(self,path,dirs):
        if not(os.path.isdir(path+"/"+dirs[0]))  :
            os.mkdir(path+"/"+dirs[0])

        if not(not(dirs[1::])):
            dir = list(dirs[1::])    
            self.makedir(path+"/"+dirs[0],dir)            
