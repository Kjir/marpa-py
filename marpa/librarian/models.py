from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    pages = models.IntegerField()
    published_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('published_on','title')
