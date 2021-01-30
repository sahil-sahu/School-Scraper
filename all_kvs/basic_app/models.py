from django.db import models

class Schools(models.Model):
    sch_nm = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    source = models.FileField(upload_to="")
    updated = models.DateTimeField('date_published', auto_now=True)