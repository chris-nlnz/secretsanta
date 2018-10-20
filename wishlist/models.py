from django.db import models
from django.urls import reverse

from secretsanta.utils import NULLABLE


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return "{}: {} at {}".format(self.date, self.name, self.location)

    def get_absolute_url(self):
        return reverse('event', args=[self.pk, ])


class Participant(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    event = models.ForeignKey('wishlist.Event', on_delete=models.CASCADE)
    buys_present_for = models.ForeignKey(
        'wishlist.Participant', on_delete=models.SET_NULL, **NULLABLE
    )

    def __str__(self):
        return "{} ({})".format(self.user, self.event.name)


class WishedItem(models.Model):
    participant = models.ForeignKey('wishlist.Participant', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField(**NULLABLE)
    scratched_off_by = models.ForeignKey(
        'wishlist.Participant', related_name="scratched_offs",
        on_delete=models.SET_NULL, **NULLABLE
    )
