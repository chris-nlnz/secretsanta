from datetime import date

from django.contrib.auth.models import User

from wishlist.draw import perform_draw
from wishlist.models import Event, Participant

eventname = "Secret Santa Friar/Luey/Asi/Van Egmond"
people = [
    ("lisa", "Lisa"),
    ("kisena", "Kisena"),
    ("tony", "Tony"),
    ("zureen", "Zureen"),
    ("paulanddiane", "Pual and Di"),
    ("brett", "Brett"),
    ("chrissy", "Chrissy"),
    ("chris", "Chris")
]
USER_EXCLUSIONS = {
    'chris': ['chrissy'],
    'chrissy': ['chris'],
    'lisa': ['kisena'],
    'kisena': ['lisa'],
    'tony': ['zureen'],
    'zureen': ['zureen']
}


def clear_data():
    Event.objects.all().delete()
    User.objects.exclude(username='chris').delete()
    Participant.objects.all().delete()


def generate_event():
    christmas = date(year=2018, month=12, day=25)
    event, _ = Event.objects.get_or_create(name=eventname, location="Taupo", date=christmas)

    for name in people:
        user, _ = User.objects.get_or_create(username=name[0], defaults={'first_name': name[1]})
        _, _ = Participant.objects.get_or_create(user=user, event=event)

    perform_draw(event, USER_EXCLUSIONS)
