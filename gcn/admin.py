from django.contrib import admin
from gcn.models import Club, Night, NightAdmin

# Register your models here.

admin.site.register(Club)
admin.site.register(Night, NightAdmin)

class NightAdmin(admin.ModelAdmin):
    list_display = ('night_name', 'club_list')


