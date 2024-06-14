from django.urls import path

from mailings.apps import MailingsConfig

app_name = MailingsConfig.name


urlpatterns = [
    # path('', MailingListView.as_view(), name='mailings_list'),
]
