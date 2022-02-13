from django.contrib import admin

# Register your models here.
from .models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_blocked')
    list_filter = ('is_blocked',)


admin.site.register(Users, UserAdmin)
