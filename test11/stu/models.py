from django.db import models

# Create your models here.

class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    score = models.DecimalField(max_digits=4,decimal_places=1)
    cls = models.ForeignKey(Clazz,on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Student:{}'.format(self.sname)
