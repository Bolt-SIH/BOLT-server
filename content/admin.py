from django.contrib import admin
from content import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk" , "Category" , "age"]


admin.site.register(models.Article)
admin.site.register(models.Category , CategoryAdmin)