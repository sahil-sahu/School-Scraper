from scrapyd_api import ScrapydAPI
from django.db.models import Q
from .models import Schools

scrapyd = ScrapydAPI('http://localhost:6800')
count = 1

regions = ['KVS Head Quarter', 'Agra', 'Ahmedabad', 'Bangalore', 'Bhopal', 'Bhubaneshwar', 'Bhubaneswar', 'Chandigarh', 'Chennai', 'Dehradun', 'Delhi', 'Ernakulam', 'Gurgaon', 'Guwahati', 'Hyderabad', 'Jabalpur', 'Jaipur', 'Jammu', 'Kolkata', 'Lucknow', 'Mumbai', 'Patna', 'Raipur', 'Ranchi', 'Silchar', 'Tinsukia', 'Varanasi', 'ZIET Bhubaneshwar', 'ZIET Chandigarh', 'ZIET Gwalior', 'ZIET Mumbai', 'ZIET Mysore']

def startit():
    global count
    
    data = []
    if count == 31:
        count = 0
    obj = Schools.objects.filter(Q(region__icontains=regions[count]))
    for i in obj:
        data.append(i.link)
    print('\n'.join(data))
    count+=1
    # task = scrapyd.schedule('school_scraper', 'get_kv', links = '\n'.join(data))

def updateit():
    global count
    data = []
    if count == 31:
        count = 0
    obj = Schools.objects.filter(Q(region__icontains=regions[count]))
    for i in obj:
        data.append(i.link)
    task = scrapyd.schedule('school_scraper', 'get_kv', links = '\n'.join(data))
    print("gone to scrapy")
    count+=1
    