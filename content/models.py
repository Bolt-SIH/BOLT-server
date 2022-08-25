from random import choice
from django.db import models

class Category(models.Model):
    Category = models.CharField(max_length=32, help_text="StartUp")
    AGE_CHOICES = (
    ('12-16', '12-16'),   # Mandate initiated
    ('17-24' , '17-24'),
    ('24+', '24+'), 
    ('All' , "All")  # Mandate successfully created
    )
    age = models.CharField(
        max_length=32, choices=AGE_CHOICES, default='PENDING')


    def __str__(self) -> str:
        return self.Category


class Article(models.Model):
    title = models.CharField( max_length=1000 , null = True , blank= True)
    source = models.CharField( max_length=100 , blank= True , null = True)
    sourceURL = models.URLField( max_length=500 , null = True ,  blank = True)
    image = models.ImageField(upload_to="article/",null = True , blank = True , height_field=None, width_field=None, max_length=None)
    description = models.TextField(blank= True , null = True)

    tags = models.ManyToManyField(Category, blank = True , null = True);

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.title




class news(models.Model):
    title = models.CharField( max_length=1000 , null = True , blank= True)
    source = models.CharField( max_length=100 , blank= True , null = True)
    sourceURL = models.URLField( max_length=500 , null = True ,  blank = True)
    image = models.ImageField(upload_to="article/",null = True , blank = True , height_field=None, width_field=None, max_length=None)
    description = models.TextField(blank= True , null = True)

    tags = models.ManyToManyField(Category, blank = True , null = True);

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.title



class books(models.Model):
    title = models.CharField( max_length=1000 , null = True , blank= True)
    source = models.CharField( max_length=100 , blank= True , null = True)
    sourceURL = models.URLField( max_length=500 , null = True ,  blank = True)
    image = models.ImageField(upload_to="article/",null = True , blank = True , height_field=None, width_field=None, max_length=None)
    description = models.TextField(blank= True , null = True)

    tags = models.ManyToManyField(Category, blank = True , null = True);

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.title


