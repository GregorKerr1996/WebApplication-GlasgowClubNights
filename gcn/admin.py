from django.contrib import admin
from gcn.models import Club, Night, NightAdmin
from gcn.models import UserProfileForm
from gcn.models import UserPictureForm
from gcn.models import UserForm

# Register your models here.

admin.site.register(Club)
admin.site.register(Night, NightAdmin)
admin.site.register(UserProfileForm)
admin.site.register(UserPictureForm)
admin.site.register(UserForm)

class NightAdmin(admin.ModelAdmin):
    list_display = ('night_name', 'club_list')
