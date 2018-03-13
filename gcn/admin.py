from django.contrib import admin
from gcn.models import Club, Night, NightAdmin
from gcn.models import userprofile

# Register your models here.

admin.site.register(Club)
admin.site.register(Night, NightAdmin)
admin.site.register(userprofile)


class NightAdmin(admin.ModelAdmin):
    list_display = ('night_name', 'club_list')
