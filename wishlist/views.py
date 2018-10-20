from django.views.generic import TemplateView

from wishlist.models import Participant


class HomeView(TemplateView):
    template_name = 'dashboard.html'

