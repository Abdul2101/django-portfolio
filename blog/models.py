from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=85)
    date = models.DateField()
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title
