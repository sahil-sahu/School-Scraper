from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from . import go_scrapy
        
def starter():
        scheduler = BackgroundScheduler()
        scheduler.add_job(go_scrapy.startit, 'interval', seconds=30)
        # scheduler.add_job(go_scrapy.updateit, 'interval', minutes=45)
        scheduler.start()