from django.apps import AppConfig


class ScheduleMail(AppConfig):
    name = 'potential_app.mailing_script.sending_mail_schedule'

    def ready(self):
        from . import scheduler
        scheduler.start()
