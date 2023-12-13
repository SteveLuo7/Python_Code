from django.db import models
from django.db.models import Manager, QuerySet


# Create your models here.
class CustomManager(Manager):
    # def all(self):
    #     return Manager.all(self).filter(isdelete=False)
    def get_queryset(self):
        return Manager.get_queryset(self).filter(isdelete=False)
#
# class DeletedManager(Manager):
#     def get_queryset(self):
#         return Manager.get_queryset(self).filter(isdelete=True)

# class CustomManager(Manager):
#     def get_queryset(self):
#         return Manager.get_queryset(self).filter(isdelete=False)
    # def filter(self, *args, **kwargs):
    #     delList = Manager.filter(self,*args,**kwargs)
    #
    #     def delete1(dlist):
    #         for d in dlist:
    #             d.isdelete = True
    #             d.save()
        #
        # import new
        # delList.delete = new.instancemethod(delete1,delList,QuerySet)
        # return delList
        #


class Student(models.Model):
    sname = models.CharField(max_length=30)
    isdelete = models.BooleanField(default=False)

    objects = CustomManager()
    # deleteM = DeletedManager()

    #   Single elements logic delete
    # def delete(self, using=None, keep_parents=False):
    #     self.isdelete = True
    #     self.save()
    class Meta:
        db_table = 't_student'

    def __unicode__(self):
        return 'Student:%s'%self.sname

# Student.objects.filter().delete()

# def insertStu(sname,cname,coursenames):