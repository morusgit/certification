from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'phone', 'city']
    list_display = ['username', 'email', 'phone', 'city']
    list_filter = ['username', 'city']

