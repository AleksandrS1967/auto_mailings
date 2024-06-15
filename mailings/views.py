from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from mailings.models import Mailing, MailingMessage, RecipientClient, HistoryMailing
from mailings.forms import MailingUpdateForm, MailingMessageUpdateForm, RecipientClientUpdateForm, \
    MailingUpdateModeratorForm


# Create your views here.
class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        if user.has_perm('mailings.can_view_mailings') or user.is_superuser:
            mailings = Mailing.objects.all()
        else:
            mailings = Mailing.objects.filter(owner=user)
        context['mailings_list'] = mailings
        return context


class MailingMessageListView(LoginRequiredMixin, ListView):
    model = MailingMessage

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        if user.has_perm('mailings.can_view_mailings') or user.is_superuser:
            messages = MailingMessage.objects.all()
        else:
            messages = MailingMessage.objects.filter(owner=user)
        context['messages'] = messages
        return context


class RecipientClientListView(LoginRequiredMixin, ListView):
    model = RecipientClient

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        clients = RecipientClient.objects.filter(owner=user)
        context['clients'] = clients
        return context


class MailingHistoryListView(LoginRequiredMixin, ListView):
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

    def get_form_class(self):
        user = self.request.user
        print(user.groups == 'moderator')
        if user == self.object.owner:
            return MailingUpdateForm
        if user.has_perm('mailings.can_edit_mailings_status'):
            return MailingUpdateModeratorForm
        raise PermissionDenied


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

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class MailingMessageCreateView(CreateView):
    model = MailingMessage
    form_class = MailingMessageUpdateForm
    success_url = reverse_lazy('mailings:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class RecipientClientCreateView(CreateView):
    model = RecipientClient
    form_class = RecipientClientUpdateForm
    success_url = reverse_lazy('mailings:clients_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


