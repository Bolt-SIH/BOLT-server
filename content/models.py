from django.db import models

class Category(models.Model):
    Category = models.CharField(max_length=32, help_text="StartUp")

    def __str__(self) -> str:
        return self.Category


class Article(models.Model):
    title = models.CharField( max_length=1000 , null = True , blank= True)
    source = models.CharField( max_length=100 , blank= True , null = True)
    sourceURL = models.URLField( max_length=500 , null = True ,  blank = True)
    image = models.ImageField(upload_to="images/article/",null = True , blank = True , height_field=None, width_field=None, max_length=None)
    description = models.TextField(blank= True , null = True)

    tags = models.ManyToManyField(Category, blank = True , null = True);

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.title

