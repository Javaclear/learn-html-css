from django.shortcuts import render
from django.http import HttpResponse

# 定义一个首页视图
from myfirstweb.models import Articles
def index(request):
    articlelist = Articles.objects.all()
    return render(request,'myfirstweb/index.html',{'articles':articlelist})

# 定义一个文章详情页
def detail(request):
    articlelist = {
        "aheadline":Articles.aheadline,
        "adescription":Articles.adescription,
    }
    return render(request,'myfirstweb/detail.html',{'articles':articlelist})
