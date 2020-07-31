from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib import messages
from .models import Article

# Create your views here.


def blogView(request):
    #articles  = Article.objects.all()
    articles = Article.objects.all()
    return render(request,"blog.html",{"articles":articles })



def detail(request,id):
    #article  = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    return render(request,"detail.html",{"article":article})


