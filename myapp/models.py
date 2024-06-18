from django.db import models
from django.urls import reverse

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=2000)
    is_published=models.BooleanField(default=True)
    time_update = models.DateTimeField(auto_now=True)
    photo=models.ImageField('photo=photo/%Y/%n/%d/')
    category=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"
    

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.CharField(max_length=50)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
    
