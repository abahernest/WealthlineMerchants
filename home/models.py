from django.db import models
from image_optimizer.fields import OptimizedImageField

# Create your models here.
class Blog (models.Model):
    image=OptimizedImageField(optimized_image_output_size=(584,396),optimized_image_resize_method='cover')
    title=models.TextField()
    story=models.TextField()
    date=models.DateTimeField(auto_now=True)
    publisher= models.CharField(max_length=200)


    def summary (self):
        return self.story[:200]+"..."

    def pretty_date (self):
        return self.date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

class RAGP_Carousel (models.Model):
    image=OptimizedImageField(optimized_image_output_size=(584,396),optimized_image_resize_method='cover')
    text=models.TextField()
    Button_text=models.CharField(max_length=20)
    link=models.URLField()

    def __str__(self):
        return self.text[:50]

class RAGP_Stories (models.Model):
    passport=OptimizedImageField(optimized_image_output_size=(584,396),optimized_image_resize_method='cover')
    name=models.CharField(max_length=50)
    story=models.TextField()

    def __str__(self):
        return self.name

    def summary (self):
        return self.story[:200]+" ..."

        





   
    
    