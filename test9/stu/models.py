from django.db import models

# Create your models here.
class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    class Meta:
        db_table = 't_cls'

    def __unicode__(self):
        return 'Clazz:%s'%self.cname

class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=30)

    class Meta:
        db_table = 't_course'
    def __unicode__(self):
        return 'Course:%s'%self.coursename

class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cls = models.ForeignKey(Clazz,on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    from django.db.transaction import atomic

    # @atomic
    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     try:
    #         self.cls = Clazz.objects.get(cname=self.cls.cname)
    #     except Clazz.DoesNotExist:
    #         self.cls = Clazz.objects.create(self)
    #     1/0
    #     return models.Model.save(self)
    #

    class Meta:
        db_table = 't_student'
    def __unicode__(self):
        return 'Student:%s'%self.sname

def insetStu(sname,cname,coursenames):
    #   Register Core Function
    try:
        try:
            cls = Clazz.objects.get(cname=cname)
        except Clazz.DoesNotExist:
            cls = Clazz.objects.create(cname=cname)

        try:
            stu = Student.objects.get(sname=sname)
        except Student.DoesNotExist:
            stu = Student.objects.create(sname=sname,cls=cls)

        courseList = []
        for cn in coursenames:
            try:
                course = Course.objects.get(coursename=cn)
            except Course.DoesNotExist:
                course = Course.objects.create(couresname=cn)
            courseList.append(course)
        stu.course.add(courseList)
        return True
    except:
        return True


