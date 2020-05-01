from django.db import models
from image_optimizer.fields import OptimizedImageField

# Create your models here.
class RAGP_Carousel (models.Model):
    image=OptimizedImageField(upload_to='RAGP/carousel/',optimized_image_output_size=(584,396),optimized_image_resize_method='cover')
    text=models.TextField()
    Button_text=models.CharField(max_length=20)
    link=models.URLField()

    def __str__(self):
        return self.text[:50]
