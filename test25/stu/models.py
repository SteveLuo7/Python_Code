from django.db import models

# Create your models here.
class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30,unique=True,verbose_name='Class Name')

    def __unicode__(self):
        return self.cname

    class Meta:
        db_table = 't_cls'

        verbose_name_plural = 'Class table'

class Student(models.Model):
    sno = models.AutoField(primary_key=True,verbose_name='Student Number')
    sname = models.CharField(max_length=30,unique=True,verbose_name='Name')
    cls = models.ForeignKey(Clazz,on_delete=models.CASCADE,verbose_name='Class belong')

    def __unicode__(self):
        return self.sname

    class Meta:
        db_table = 't_student'
        verbose_name_plural = 'Student table'
