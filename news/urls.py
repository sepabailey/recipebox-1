from django.urls import path
from news import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('addrecipe/', views.addrecipe),
    path('addauthor/', views.addauthor),
    path("author/<int:id>", views.author),
    path("recipe/<int:id>", views.recipe, name='recipe'),
    path('login/', views.loginview, name='login'),
    path('create_user/', views.create_user),
    path('logout_view/', views.logout_view),
    path('recipe/edit/<int:id>/', views.edit_recipe, name='edit_recipe'),
    path('favorite/<int:id>', views.favorite_view, name='favorite'),
    path('unfavorite/<int:id>', views.unfavorite_view, name='unfavorite'),

    # path('admin/', admin.site.urls),
]