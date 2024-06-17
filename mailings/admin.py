from django.contrib import admin
from mailings.models import (Mailing, MailingMessage,
                             RecipientClient, HistoryMailing)


# Register your models here.
@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("first_date", "periodicity", "status", "message")


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ("theme", "body")


@admin.register(RecipientClient)
class RecipientClientAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "comment")


@admin.register(HistoryMailing)
class HistoryMailingAdmin(admin.ModelAdmin):
    list_display = ("last_date", "status", "response")
