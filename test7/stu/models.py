from django.db import models

# Create your models here.
class Goods(models.Model):
    goodisd = models.AutoField(primary_key=True)
    gname = models.CharField(max_length=30)
    gdesc = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    count = models.PositiveIntegerField()
    created = models.DateField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    gimg = models.ImageField(upload_to='images/')
