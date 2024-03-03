from django.contrib import admin

from .models import good


@admin.register(good)
class goodAdmin(admin.ModelAdmin):
    list_display= ("title", "isbn", "Supplier", "weight")
    list_filter =("Supplier", "weight")

