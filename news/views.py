from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from news.models import Recipe, Author
from news.forms import AddRecipeForm, AddAuthorForm, LoginForm


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']

            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

@login_required
def addrecipe(request):
    html = "generic_form.html"
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

@login_required
def addauthor(request):
    html = "generic_form.html"
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
