from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
def  home(request):
    post_lsit = Article.objects.all()
    return render(request,'base.html',{'post_list':post_lsit})

def detail(request,id):
    post = Article.objects.all()[int(id)]
    gstr = ('title is %s,category is %s,content is %s')%(post.title,post.category,post.content) 
    return HttpResponse(gstr)
def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})