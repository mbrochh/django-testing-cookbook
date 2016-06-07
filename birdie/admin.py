from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['excerpt', ]

    def excerpt(self, obj):
        return obj.get_excerpt(5)
admin.site.register(models.Post, PostAdmin)
