from django.contrib import admin

from .models import Room, Player


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'uuid')


admin.site.register(Room, RoomAdmin)
admin.site.register(Player, PlayerAdmin)
