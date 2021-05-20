from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    slug = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Photo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    image = models.ImageField(null=False, blank=False)
    slug = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField()
    

    def __str__(self):
        return str(self.name)