from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.forms import PublicationForm
from blog.models import Publication
from config.settings import EMAIL_HOST_USER


# Create your views here.
class PublicationCreateView(CreateView):
    model = Publication
    form_class = PublicationForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)


class PublicationListView(LoginRequiredMixin, ListView):
    model = Publication

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_activ=True)
        return queryset


class PublicationDetailView(DetailView):
    model = Publication

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.counter += 1
        self.object.save()
        if self.object.counter >= 100:
            send_mail(
                'Просмотры Блога',
                f'Ура! - публикация <{self.object}> набрала 100 просмотров...',
                EMAIL_HOST_USER,
                ['sanyastronger@rambler.ru', ],
            )
        return self.object


class PublicationUpdateView(PermissionRequiredMixin, UpdateView):
    model = Publication
    form_class = PublicationForm
    permission_required = 'blog.change_publication'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class PublicationDeleteView(PermissionRequiredMixin, DeleteView):
    model = Publication
    success_url = reverse_lazy('blog:list')
    permission_required = 'blog.delete_publication'
