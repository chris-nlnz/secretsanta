import random
import string

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


def _random_code():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


class Participant(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    event = models.ForeignKey('wishlist.Event', on_delete=models.CASCADE)
    buys_present_for = models.ForeignKey(
        'wishlist.Participant', on_delete=models.SET_NULL, **NULLABLE
    )
    unique_code = models.CharField(unique=True, db_index=True, max_length=16, blank=True, null=True)

    def __str__(self):
        return self.user.first_name or self.user.username

    def simple_draw_url(self):
        return reverse('simple_draw', args=[self.unique_code, ])

    def save(self, *args, **kwargs):
        if not self.unique_code:
            while True:
                code = _random_code()
                if not Participant.objects.filter(unique_code=code).exists():
                    self.unique_code = code
                    break
        super(Participant, self).save()


class WishedItem(models.Model):
    participant = models.ForeignKey('wishlist.Participant', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField(**NULLABLE)
    scratched_off_by = models.ForeignKey(
        'wishlist.Participant', related_name="scratched_offs",
        on_delete=models.SET_NULL, **NULLABLE
    )
