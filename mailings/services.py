import smtplib

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime as dt
import pytz
from django.conf import settings
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


def sending_messages():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = dt.now(zone)
    from mailings.models import Mailing, HistoryMailing
    mailings = Mailing.objects.filter(status='запущена')
    print(f'\nКоличество рассылок для отправки: {mailings.count()}')
    print(f'Сейчас - {current_datetime}')
    for mailing in mailings:
        mailing.status = 'запущена'
        if mailing.check_periodicity == 0:
            clients = mailing.clients.all()
            client_emails = [client.email for client in clients]
            print(f'Клиенты получатели - {client_emails}')
            try:
                response = send_mail(
                    mailing.message.theme,
                    mailing.message.body,
                    EMAIL_HOST_USER,
                    client_emails,
                    fail_silently=False,
                )
                HistoryMailing.objects.create(last_date=current_datetime,
                                              status=True,
                                              response=response, )
            except smtplib.SMTPException as e:
                mailing.status = 'завершена'
                print(f'Непредвиденная ошибка{e}')
                HistoryMailing.objects.create(last_date=current_datetime,
                                              status=False,
                                              response=str(e), )
            if mailing.periodicity == 'раз в день':
                mailing.check_periodicity = 1
            if mailing.periodicity == 'раз в неделю':
                mailing.check_periodicity = 7
            if mailing.periodicity == 'раз в месяц':
                mailing.check_periodicity = 30
        else:
            mailing.check_periodicity = mailing.check_periodicity - 1
        mailing.save()


def start_apscheduler():
    print('Starting scheduler...')
    scheduler = BackgroundScheduler()
    if not scheduler.running:
        scheduler.add_job(sending_messages, 'interval', seconds=10)
        scheduler.start()
        print('Scheduler запущен успешно')


