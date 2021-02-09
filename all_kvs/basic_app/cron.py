from scrapyd_api import ScrapydAPI
from django.db.models import Q
from .models import Schools, Scrapy_Switch

scrapyd = ScrapydAPI('http://localhost:6800')
count = 1

regions = ['KVS Head Quarter', 'Agra', 'Ahmedabad', 'Bangalore', 'Bhopal', 'Bhubaneshwar', 'Bhubaneswar', 'Chandigarh', 'Chennai', 'Dehradun', 'Delhi', 'Ernakulam', 'Gurgaon', 'Guwahati', 'Hyderabad', 'Jabalpur',
           'Jaipur', 'Jammu', 'Kolkata', 'Lucknow', 'Mumbai', 'Patna', 'Raipur', 'Ranchi', 'Silchar', 'Tinsukia', 'Varanasi', 'ZIET Bhubaneshwar', 'ZIET Chandigarh', 'ZIET Gwalior', 'ZIET Mumbai', 'ZIET Mysore']


def checker():
    boo = Scrapy_Switch.objects.all()[0]
    return boo.switch


def startit():
    global count
    if checker():
        data = []
        if count == 31:
            count = 0
        obj = Schools.objects.filter(Q(region__icontains=regions[count]))
        for i in obj:
            data.append(i.link)
        print('\n'.join(data))
        count += 1
        # task = scrapyd.schedule('school_scraper', 'get_kv', links = '\n'.join(data))


def updateit():
    global count
    if checker():
        data = []
        if count == 31:
            count = 0
        obj = Schools.objects.filter(Q(region__icontains=regions[count]))
        for i in obj:
            data.append(i.link)
        task = scrapyd.schedule(
            'school_scraper', 'get_kv', links='\n'.join(data))
        print("gone to scrapy")
        count += 1
