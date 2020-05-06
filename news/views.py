from django.shortcuts import render

from news.models import NewsItem, Author

# Create your views here.
def index(request):
    data = NewsItem.objects.all()
    return render(request, 'index.html', {'data': data})

def author(request, id):
    author = Author.objects.get(id=id)
    recipes = NewsItem.objects.filter(author=author)
    return render(request, 'author.html', {
        'author': author, 'recipes': recipes})
    
def recipe(request, id):
    
    recipes = NewsItem.objects.get(id=id)
    return render(request, 'recipes.html', {
        'recipe': recipes})
