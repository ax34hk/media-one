from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    name_ar = models.CharField(max_length=50)
    is_movie = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
	    verbose_name_plural = 'categories'


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=128)
    title_ar = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=250)
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    link1 = models.CharField(max_length=250, blank=True, null=True)
    link2 = models.CharField(max_length=250, blank=True, null=True)
    link3 = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Serie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=250)
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_tvshow = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Episode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=8)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    link1 = models.CharField(max_length=250, blank=True, null=True)
    link2 = models.CharField(max_length=250, blank=True, null=True)
    link3 = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
