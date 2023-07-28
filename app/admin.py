from django.contrib import admin
from .models import Movie, Serie, Episode, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

admin.site.register(Movie)
admin.site.register(Serie)
admin.site.register(Episode)
admin.site.register(Category, CategoryAdmin)

