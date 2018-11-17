from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from wishlist.models import Event, Participant


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = "event"
    template_name = "event.html"


def simple_draw_view(request, participant_code):
    """Change this to a CBV in due time.. too lazy to do it now"""
    participant = get_object_or_404(Participant, unique_code=participant_code)
    return render(request, 'wishlist/simple-draw-view.html', {
        'participant': participant
    })