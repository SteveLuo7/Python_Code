from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=30,unique=True,verbose_name=u'类别名称')

    def __str__(self):
        return '<category:%s>' % self.cname

    class Meta:
        db_table = 't_category'
        verbose_name_plural = u'类别'

class Tag(models.Model):
    tname = models.CharField(max_length=20,unique=True,verbose_name=u'标签名称')

    def __str__(self):
        return '<tag:%s>'%self.tname

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = u'标签'

class Post(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name=u'标题')
    desc = models.CharField(max_length=200,verbose_name=u'简介')
    content = models.TextField(verbose_name=u'正文')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False,verbose_name=u'是否删除')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=u'所属类别')
    tag = models.ManyToManyField(Tag,verbose_name=u'标签')

    def __str__(self):
        return '<post:%s>'%self.title

    class Meta:
        db_table = 't_post'
        verbose_name_plural = u'帖子'


