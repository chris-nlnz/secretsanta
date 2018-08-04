from django.db import models

from secretsanta.utils import NULLABLE

class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()


class Participant(models.Model):
    user = models.ForeignKey('django.contrib.auth.User')
    event = models.ForeignKey('wishlist.Event')
    buys_present_for = models.ForeignKey('wishlist.Participant')


class WishedItem(models.Model):
    participant = models.ForeignKey('wishlist.Participant')
    name = models.CharField(max_length=255)
    url = models.URLField(**NULLABLE)
    scratched_off_by = models.ForeignKey('wishlist.Participant')



