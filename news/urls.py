from django.urls import path
from news import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('addrecipe/', views.addrecipe),
    path('addauthor/', views.addauthor),
    path("author/<int:id>", views.author),
    path("recipe/<int:id>", views.recipe),
    path('login/', views.loginview)

    # path('admin/', admin.site.urls),
]