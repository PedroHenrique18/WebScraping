from django.db import models

class URL(models.Model):
    url = models.URLField(unique=True)
    last_scraped = models.DateTimeField(null=True, blank=True)
    
