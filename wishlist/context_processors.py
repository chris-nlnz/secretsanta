from wishlist.models import Participant


def participation_events(request):
    """Returns all events the current user is participating in"""
    if request.user.is_authenticated:
        return {
            'participations': Participant.objects.filter(
                user=request.user
            ).order_by('event__date')
        }
    else:
        return {}
