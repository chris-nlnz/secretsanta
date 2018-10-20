from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView

from wishlist.models import Event


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = "event"
    template_name = "event.html"
