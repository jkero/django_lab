from django.contrib import admin

# Register your models here.

from .models import LeParam1

class Param1Admin(admin.ModelAdmin):
    fieldsets = [
        ("Le param1", {"fields": ["param_nom"]}),
        ("Date information", {"fields": ["param_date"], "classes": ["collapse"]})
    ]

    list_display = ["param_nom", "param_date"]
    list_filter = ["param_date"]
    search_fields = ["param_nom"]

admin.site.register(LeParam1, Param1Admin)