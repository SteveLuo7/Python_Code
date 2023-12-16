from django.db import models

# Create your models here.
class Studen(models.Model):
    sname = models.CharField(max_length=30)

    def __unicode__(self):
        return self.sname
