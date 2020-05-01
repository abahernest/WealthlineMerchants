from django.shortcuts import render,get_object_or_404
from .models import RAGP_Carousel

# Create your views here.
def HomeViews (request):
    carousels=RAGP_Carousel.objects.all()[1:]
    firstcarousel=RAGP_Carousel.objects.all()[0]

    context= {'carousels':carousels,'firstcarousel':firstcarousel}
    return render (request,'home/index.html', context)