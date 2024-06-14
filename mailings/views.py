
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from mailings.models import Mailing, MailingMessage, RecipientClient, HistoryMailing
from mailings.forms import MailingUpdateForm, MailingMessageUpdateForm, RecipientClientUpdateForm


# Create your views here.
class MailingListView(ListView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        mailings = Mailing.objects.all()
        context['mailings_list'] = mailings
        return context


class MailingMessageListView(ListView):
    model = MailingMessage

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        messages = MailingMessage.objects.all()
        context['messages'] = messages
        return context


class RecipientClientListView(ListView):
    model = RecipientClient

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        clients = RecipientClient.objects.all()
        context['clients'] = clients
        return context


class MailingHistoryListView(ListView):
    model = HistoryMailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        history = HistoryMailing.objects.all()
        context['history'] = history
        return context


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingUpdateForm
    success_url = reverse_lazy('mailings:mailings_list')

    def get_success_url(self):
        return reverse('mailings:mailing_detail', args=[self.kwargs.get('pk')])


class MailingMessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MailingMessageUpdateForm
    success_url = reverse_lazy('mailings:message_list')

    def get_success_url(self):
        return reverse('mailings:message_detail', args=[self.kwargs.get('pk')])


class RecipientClientUpdateView(UpdateView):
    model = RecipientClient
    form_class = RecipientClientUpdateForm
    success_url = reverse_lazy('mailings:clients_list')

    def get_success_url(self):
        return reverse('mailings:clients_detail', args=[self.kwargs.get('pk')])


class MailingDetailView(DetailView):
    model = Mailing


class MailingMessageDetailView(DetailView):
    model = MailingMessage


class RecipientClientDetailView(DetailView):
    model = RecipientClient


class MailingHistoryDetailView(DetailView):
    model = HistoryMailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailings_list')


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailings:message_list')


class RecipientClientDeleteView(DeleteView):
    model = RecipientClient
    success_url = reverse_lazy('mailings:clients_list')


class MailingHistoryDeleteView(DeleteView):
    model = HistoryMailing
    success_url = reverse_lazy('mailings:history_list')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingUpdateForm
    success_url = reverse_lazy('mailings:mailings_list')


class MailingMessageCreateView(CreateView):
    model = MailingMessage
    form_class = MailingMessageUpdateForm
    success_url = reverse_lazy('mailings:message_list')


class RecipientClientCreateView(CreateView):
    model = RecipientClient
    form_class = RecipientClientUpdateForm
    success_url = reverse_lazy('mailings:clients_list')
