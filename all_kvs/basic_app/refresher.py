from apscheduler.schedulers.background import BackgroundScheduler
from . import cron

scheduler = BackgroundScheduler()
scheduler.start()


def start():
    global scheduler
    # scheduler.add_job(cron.startit, 'interval', seconds=3)
    # scheduler.add_job(cron.startit, 'interval', hours=23)
    scheduler.add_job(cron.updateit, 'interval', seconds=50)
