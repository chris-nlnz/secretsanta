from datetime import date

from django.contrib.auth.models import User

from wishlist.models import Event, Participant

eventname = "Secret Santa Friar/Luey/Asi/Van Egmond"
people = ["lisa", "kisena", "tony", "zureen", "paul", "diane", "brett", "chrissy", "chris"]


def generate_event():
    christmas = date(year=2018, month=12, day=25)
    event, _ = Event.objects.get_or_create(name=eventname, location="Taupo", date=christmas)

    for name in people:
        user, _ = User.objects.get_or_create(username=name)
        _, _ = Participant.objects.get_or_create(user=user, event=event)
