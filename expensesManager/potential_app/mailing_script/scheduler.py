from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from potential_app.mailing_script.statsmsg_conf import sender


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "newJobStore")
    # 'hour' states at what time each day to send messages
    scheduler.add_job(sender, 'cron', hour=10, name='mailsender', jobstore='newJobStore')
    scheduler.start()
    print("Mail sender started")