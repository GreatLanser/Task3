from django.contrib import admin

# Register your models here.
from .models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'status')
    list_filter = ('status',)


admin.site.register(Users, UserAdmin)
