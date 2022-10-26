from django.db import models
from django.urls import reverse
import datetime
class Book(models.Model):
    name = models.CharField(max_length=50)
    athor = models.CharField(max_length=50)
    date = models.DateField('date published')
    text = models.TextField()
    accept = models.BooleanField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.accept is None:
            self.accept=False
        if self.date is None:
            self.date = datetime.date
    def __str__(self):
        return f"{str(self.name)}. {str(self.athor)}"
    def get_absolute_url(self):
        return reverse('books:lists')
