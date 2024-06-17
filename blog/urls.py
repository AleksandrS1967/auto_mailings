from django.urls import path

from blog.apps import BlogConfig
from django.views.decorators.cache import cache_page
from blog.views import (
    PublicationCreateView,
    PublicationListView,
    PublicationDetailView,
    PublicationUpdateView,
    PublicationDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("create/", PublicationCreateView.as_view(), name="create"),
    path("", cache_page(60)(PublicationListView.as_view()), name="list"),
    path("view/<int:pk>", PublicationDetailView.as_view(), name="view"),
    path("edit/<int:pk>", PublicationUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>", PublicationDeleteView.as_view(), name="delete"),
]
