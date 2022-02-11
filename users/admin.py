from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'status')
    list_filter = ('status',)


admin.site.register(User, UserAdmin)
