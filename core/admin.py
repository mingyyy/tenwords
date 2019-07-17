from django.contrib import admin
from .models import Tag, Responder


class ResponderAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "email")


admin.site.register(Tag)
admin.site.register(Responder, ResponderAdmin)