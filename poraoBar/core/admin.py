from django.contrib import admin
from .models import Email

class EmailModelAdmin(admin.ModelAdmin):
    list_display = ('mail', 'created_at')
    date_hierarchy = 'created_at'
admin.site.register(Email, EmailModelAdmin)

