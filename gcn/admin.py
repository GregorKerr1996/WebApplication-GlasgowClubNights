from django.contrib import admin
from gcn.models import Club, Night, NightAdmin
from gcn.models import UserProfileForm
from gcn.models import UserPictureForm
from gcn.models import UserForm
from gcn.models import UserReviewForm


# Register your models here.

admin.site.register(Club)
admin.site.register(Night, NightAdmin)
admin.site.register(UserProfileForm)
admin.site.register(UserPictureForm)
admin.site.register(UserForm)
admin.site.register(UserReviewForm)


class NightAdmin(admin.ModelAdmin):
    list_display = ('night_name', 'club_list', 'night_day',)

class PageForm(admin.ModelAdmin):
    list_display = ('night_name', 'club_list')



