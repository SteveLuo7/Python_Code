from django.db import models


# Create your models here.
class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30, unique=True)
    class Meta:
        db_table = 't_cls'
    def __unicode__(self):
        return u'Clazz: %s' % self.cname



class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cls = models.ForeignKey(Clazz,on_delete=models.CASCADE)

    class Meta:
        db_table = 't_stu2'

    def __unicode__(self):
        return u'Student: %s' % self.sname