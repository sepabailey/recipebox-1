from django.contrib import admin
from news.models import Author, NewsItem
# Register your models here.
admin.site.register(NewsItem)
admin.site.register(Author)
