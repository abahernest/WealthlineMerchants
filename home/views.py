from django.shortcuts import render,get_object_or_404
from .models import Blog,RAGP_Carousel,RAGP_Stories

# Create your views here.
def HomeViews (request):
    blogs=Blog.objects.all()
    carousels=RAGP_Carousel.objects.all()[1:]
    stories=RAGP_Stories.objects.all()
    firstcarousel=RAGP_Carousel.objects.all()[0]

    context= {'blogs':blogs,'carousels':carousels,'firstcarousel':firstcarousel,'stories':stories}
    return render (request,'home/index.html', context)

def AboutViews (request):
    return render(request,'home/about.html')

def DetailViews (request, blog_title):
    blogs=get_object_or_404(Blog, title=blog_title)

    context={'blog':blogs}
    return render(request,'home/detail.html',context)

def StoryViews (request,ragp_stories_name):
    stories=get_object_or_404(RAGP_Stories, name=ragp_stories_name)

    context={'story':stories}
    return render(request,'home/stories.html',context)