from django.db import models
from uuid import uuid4

# Create your models here.


class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
