from django.shortcuts import render, reverse, HttpResponseRedirect

from news.models import Recipe, Author
from news.forms import AddRecipeForm, AddAuthorForm

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def addrecipe(request):
    html = "addrecipeform.html"

    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']

            )
            return HttpResponseRedirect(reverse('homepage'))


    form = AddRecipeForm()

    return render(request, html, {"form": form})

def addauthor(request):
    html = "addauthorform.html"


    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()


    return render(request, html, {'form': form})

def author(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author.html', {
        'author': author, 'recipes': recipes})


def recipe(request, id):

    recipes = Recipe.objects.get(id=id)
    return render(request, 'recipes.html', {
        'recipe': recipes})
