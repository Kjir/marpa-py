from django.db import models
from datetime import date

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    pages = models.IntegerField()
    published_on = models.DateField(default=date.today)

    class Meta:
        ordering = ('published_on','title')

class Patron(models.Model):
    first_name = models.CharField(max_length=100, blank=False, default='')
    last_name = models.CharField(max_length=100, blank=False, default='')

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    rent_date = models.DateField(default=date.today)
    due_date = models.DateField()
