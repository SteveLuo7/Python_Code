from django.db import models

# Create your models here.
class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=30)
    class Meta:
        db_table = 't_course'
    def __unicode__(self):
        return 'Course: {}'.format(self.coursename)

class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    course = models.ManyToManyField(Course)
    class Meta:
        db_table = 't_stu3'
    def __unicode__(self):
        return 'Student: {}'.format(self.sname)
