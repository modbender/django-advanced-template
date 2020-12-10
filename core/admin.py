from django.contrib import admin

from . import models

class BaseCoreAdmin(admin.ModelAdmin):

    class Meta:
        abstract = True

# @admin.register(BaseCoreAdmin)
# class YourAdmin(admin.ModelAdmin):
#     pass
