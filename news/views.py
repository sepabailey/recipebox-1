from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

def create_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'], password=data['password']

            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                    )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


# added login requirement so index is only visible when logged in
@login_required
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
    # fixed bug with addauthor
    html = "generic_form.html"
    # if request.user.is_staff:
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
            new_author=Author.objects.create(
                user=new_user,
                name=data['name'],
                bio=data['bio']

            )
            new_author.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = AddAuthorForm()

    return render(request, html, {'form': form})


def author(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author.html', {
        'author': author, 'recipes': recipes})


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.user.is_authenticated:
        current_author = request.user.author.favorite.all()
        return render(request, 'recipes.html', {'recipe': recipe, 'current_author': current_author})
    return render(request, 'recipes.html', {'recipe': recipe})

def favorite_view(request, id):
    current_user = request.user.author
    favorite_recipe = Recipe.objects.get(id=id)
    current_user.favorite.add(favorite_recipe)
    current_user.save()
    # Matt helped me add f string to fix path that was breaking page
    return HttpResponseRedirect(f'/recipe/{favorite_recipe.id}')


def unfavorite_view(request, id):
    current_user = request.user.author
    favorite_recipe = Recipe.objects.get(id=id)
    current_user.favorite.remove(favorite_recipe)
    current_user.save()
    # Matt helped me add f string to fix path that was breaking page
    return HttpResponseRedirect(f'/recipe/{favorite_recipe.id}')


def logout_view(request):
    logout(request)
    # Changed to login so when logout goes to login page
    return HttpResponseRedirect(reverse('login'))


def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if request.user.author == recipe.author or request.user.is_staff:
            if form.is_valid():
                data = form.cleaned_data
                recipe.title = data['title']
                recipe.author = data['author']
                recipe.description = data['description']
                recipe.time_required = data['time_required']
                recipe.instructions = data['instructions']
                recipe.save()
            return HttpResponseRedirect(reverse('recipe', args=(id,)))
    form = AddRecipeForm(initial={
        'title': recipe.title,
        'author': recipe.author,
        'description': recipe.description,
        'time_required': recipe.time_required,
        'instructions': recipe.instructions,
    })
    return render(request, 'generic_form.html', {'form': form})



