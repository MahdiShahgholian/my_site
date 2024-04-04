from django.contrib import admin
from .models import Contact, Newsletter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["name", "email", "subject", "created_date"]
    search_fields = ["name", "subject"]
    list_filter = ["name", "email"]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)