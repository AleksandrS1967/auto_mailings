from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import (MailingListView, MailingUpdateView, MailingDetailView, MailingDeleteView, MailingCreateView,
                            MailingMessageListView, MailingMessageUpdateView, MailingMessageDetailView,
                            MailingMessageDeleteView, MailingMessageCreateView, RecipientClientListView,
                            RecipientClientUpdateView, RecipientClientDetailView, RecipientClientDeleteView,
                            RecipientClientCreateView, MailingHistoryListView, MailingHistoryDetailView,
                            MailingHistoryDeleteView)

app_name = MailingsConfig.name


urlpatterns = [
    path('', MailingListView.as_view(), name='mailings_list'),
    path('message_list/', MailingMessageListView.as_view(), name='message_list'),
    path('clients_list/', RecipientClientListView.as_view(), name='clients_list'),
    path('history_list/', MailingHistoryListView.as_view(), name='history_list'),
    path('mailing_update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('message_update/<int:pk>', MailingMessageUpdateView.as_view(), name='message_update'),
    path('clients_update/<int:pk>', RecipientClientUpdateView.as_view(), name='clients_update'),
    path('mailing_detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('message_detail/<int:pk>', MailingMessageDetailView.as_view(), name='message_detail'),
    path('clients_detail/<int:pk>', RecipientClientDetailView.as_view(), name='clients_detail'),
    path('history_detail/<int:pk>', MailingHistoryDetailView.as_view(), name='history_detail'),
    path('mailing_delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    path('message_delete/<int:pk>', MailingMessageDeleteView.as_view(), name='message_delete'),
    path('clients_delete/<int:pk>', RecipientClientDeleteView.as_view(), name='clients_delete'),
    path('history_delete/<int:pk>', MailingHistoryDeleteView.as_view(), name='history_delete'),
    path('create/', MailingCreateView.as_view(), name='create_mailing'),
    path('create_message/', MailingMessageCreateView.as_view(), name='create_message'),
    path('create_client/', RecipientClientCreateView.as_view(), name='create_client')
]
