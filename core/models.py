from django.db import models
from django.conf import settings
from django.utils import timezone

from easy_thumbnails.fields import ThumbnailerImageField

class BaseCoreModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    added_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

# class YourModel(BaseCoreModel):
#     ...
