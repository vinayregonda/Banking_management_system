from django.contrib import admin

from .models import *
class AccountAdmin(admin.ModelAdmin):
    list_display = ['accountNumber', 'firstName','middleName','lastName','Email','Password','Pin','beginingBalance','created_at','last_update']
admin.site.register(Account, AccountAdmin)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display=['created_at','title','body','last_date']
admin.site.register(Announcement,AnnouncementAdmin)