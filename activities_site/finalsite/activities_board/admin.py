
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import Event, Category, User, Comment, Registrations


class EventAdmin(admin.ModelAdmin):
    list_display = ('eventName', 'content', 'startTime', 'published','eventFormat','location')
    #filter_horizontal = ('category',)
    list_display_links = ('eventName', 'content')
    search_fields = ('eventName', 'content', )


admin.site.register(Event, EventAdmin)
class UserAdmin(admin.ModelAdmin):
    # model = User
    # filter_horizontal = ('registrations',)
    # save_on_top = True
    list_display = ('name','surname', 'email')
    list_display_links = ('name', 'surname')
    search_fields = ('name', 'surname',)

# class CustomUserAdmin(UserAdmin):
#     #filter_horizontal = ('registrations',)
#     save_on_top = True
#     list_display = ('name','surname', 'email')
#     inlines = [UserInline]


admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Registrations)

