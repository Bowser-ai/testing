from django.db import models

from lists.models import List


class Item(models.Model):
    text = models.CharField(max_length=100)
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name='items'
    )
