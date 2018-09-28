from django.contrib import admin

from wishlist.models import Event, Participant, WishedItem


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')
    ordering = ('date', )
admin.site.register(Event, EventAdmin)


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'event', 'buys_present_for')
    ordering = ('event__date', )
admin.site.register(Participant, ParticipantAdmin)


class WishedItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'participant', 'name', 'url', 'scratched_off_by')
    ordering = ('participant__event__date', 'participant')
admin.site.register(WishedItem, WishedItemAdmin)
