from django.contrib import admin

from users.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']

admin.site.register(Customer, CustomerAdmin)