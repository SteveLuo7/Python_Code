import paginator
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from post.models import Post


# Create your views here.
class IndexView(View):
    def get(self,requset,num=1):
        num = int(num)
        postList = Post.objects.all()
        #   create paginator elements
        page_obj = Paginator(postList,1)
        #   get page data
        page_post = page_obj.page(num)



        return render(requset,'index.html', {'postList': page_post})
