from django.contrib import admin

from stu.models import Clazz, Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno','sname']

    list_filter = ['sno']

    search_fields = ['sno','sname']

    raw_id_fields = ['cls']

    ordering = ['sno']

admin.site.register(Clazz)
admin.site.register(Student,StudentAdmin)


