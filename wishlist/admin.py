from django.contrib import admin
from django.utils.safestring import mark_safe

from wishlist.models import Event, Participant, WishedItem


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')
    ordering = ('date', )
admin.site.register(Event, EventAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'buys_present_for', 'user', 'event', 'draw_url')
    ordering = ('event__date', )

    def draw_url(self, participant):
        url = participant.simple_draw_url()
        link = (
            '<a href="http://confidentialsanta.co.nz{0}" target="_blank">'
            'http://confidentialsanta.co.nz{0}'
            '</a>'
        ).format(url)
        return mark_safe(link)
    draw_url.short_description = 'Draw URL'
admin.site.register(Participant, ParticipantAdmin)


class WishedItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'participant', 'name', 'url', 'scratched_off_by')
    ordering = ('participant__event__date', 'participant')
admin.site.register(WishedItem, WishedItemAdmin)
