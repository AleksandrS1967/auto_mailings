import smtplib
from datetime import datetime as dt

import pytz
from django.core.mail import send_mail
from django.core.management import BaseCommand

from config import settings
from mailings.models import Mailing, HistoryMailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        функция для команды единоразового запуска рассылок
        """
        zone = pytz.timezone(settings.TIME_ZONE)
        current_datetime = dt.now(zone).date()
        mailings = Mailing.objects.filter(first_date__lte=current_datetime)
        print(f"\nКоличество рассылок для отправки: {mailings.count()}")
        print(f"Сейчас - {current_datetime}")
        for mailing in mailings:
            if mailing.status == "завершена":
                pass
            else:
                mailing.status = "запущена"
                if mailing.check_periodicity == 0:
                    clients = mailing.clients.all()
                    client_emails = [client.email for client in clients]
                    print(f"Клиенты получатели - {client_emails}")
                    try:
                        response = send_mail(
                            mailing.message.theme,
                            mailing.message.body,
                            settings.EMAIL_HOST_USER,
                            client_emails,
                            fail_silently=False,
                        )
                        HistoryMailing.objects.create(
                            last_date=current_datetime,
                            status=True,
                            response=response,
                        )
                    except smtplib.SMTPException as e:
                        mailing.status = "завершена"
                        print(f"Непредвиденная ошибка{e}")
                        HistoryMailing.objects.create(
                            last_date=current_datetime,
                            status=False,
                            response=str(e),
                        )
                    if mailing.periodicity == "раз в день":
                        mailing.check_periodicity = 1
                    if mailing.periodicity == "раз в неделю":
                        mailing.check_periodicity = 7
                    if mailing.periodicity == "раз в месяц":
                        mailing.check_periodicity = 30
                else:
                    mailing.check_periodicity = mailing.check_periodicity - 1
                mailing.save()
