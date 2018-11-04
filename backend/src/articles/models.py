from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title
