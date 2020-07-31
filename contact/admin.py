from django.contrib import admin
from .models import Contact
# Register your models here.

#admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ["name", "email", "phone", "message",'subject','created_date']

    list_display =['name', 'email', 'subject','created_date','status']

    list_filter = ['status','created_date']