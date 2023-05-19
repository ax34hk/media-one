from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    name_ar = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
	    verbose_name_plural = 'categories'


class Movie(models.Model):
    title = models.CharField(max_length=50)
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
    


