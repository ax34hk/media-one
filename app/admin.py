from django.contrib import admin
from .models import Movie, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

admin.site.register(Movie)
admin.site.register(Category, CategoryAdmin)

