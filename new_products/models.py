from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Products(models.Model):
    product_code = models.CharField(max_length=20, unique=True,default='default_code')
    name=models.CharField(max_length=20)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=0)
    # image=models.ImageField()
    image_url = models.ImageField()

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.SlugField(unique=True ,null=True ,blank=True)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse('blog_detile', args=[str(self.product_code)])
    

@receiver(pre_save,sender=Products)
def pre_save_receiver(sender,instance,*args,**kwargs):
    slug=slugify(instance.product_code)
    exists=Products.objects.filter(slug=slug).exists()
    if exists:
        slug='%s-%s'%(slug,instance.pk)
    instance.slug=slug