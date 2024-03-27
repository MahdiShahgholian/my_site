from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["name", "email_address", "subject", "created_date"]
    search_fields = ["name", "subject"]
    list_filter = ["name", "email_address"]

admin.site.register(Contact, ContactAdmin)
