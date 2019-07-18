from django.contrib import admin
from .models import Responder


class ResponderAdmin(admin.ModelAdmin):
    list_display = ("code", "age", "gender")

admin.site.register(Responder, ResponderAdmin)