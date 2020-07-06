from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import *


blogs=Blog.objects.all().order_by('-date')
carousels=RAGP_Carousel.objects.all()
stories=RAGP_Stories.objects.all().order_by('-id')



# Create your views here.
def HomeViews (request):
    context= {'blogs':blogs[:5],'carousels':carousels[1:],'firstcarousel':carousels[0],'stories':stories[:2]}
    return render (request,'home/index.html', context)

def AboutViews (request):
    return render(request,'home/about.html')

def DetailViews (request, blog_title):
    blog_detail=get_object_or_404(Blog, title=blog_title)
    comments=blog_detail.comments.filter(active=True)
    new_comment=None
    if request.method =='POST':
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post=blog_detail
            new_comment.save()
    else:
        comment_form=CommentForm()
    
    context={'blog':blog_detail,
    'comments':comments,
    'new_comment':new_comment,
    'comment_form':comment_form}
    return render(request,'home/detail.html',context)

def StoryViews (request,ragp_stories_name):
    stories_detail=get_object_or_404(RAGP_Stories, name=ragp_stories_name)

    context={'story':stories_detail}
    return render(request,'home/stories.html',context)

def MoreStoriesViews (request):
    context={'stories':stories}
    return render(request,'home/morestories.html',context)


def MorePostsViews (request):
    context={'blogs':blogs}
    return render(request,'home/moreposts.html',context)