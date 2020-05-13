from django.urls import path
from news import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('addrecipe/', views.addrecipe),
    path('addauthor/', views.addauthor),
    path("author/<int:id>", views.author),
    path("recipe/<int:id>", views.recipe),
    path('login/', views.loginview),
    path('create_user/', views.create_user),
    path('logout_view/', views.logout_view)

    # path('admin/', admin.site.urls),
]