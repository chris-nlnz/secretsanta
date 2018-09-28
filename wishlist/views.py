from django.views.generic import TemplateView

from wishlist.models import Participant


class HomeView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        return {
            'participations': Participant.objects.filter(
                user=self.request.user
            ).order_by('event__date')
        }
