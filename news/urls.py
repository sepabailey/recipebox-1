from django.urls import path
from news import views

urlpatterns = [
    path('', views.index),
    path("author/<int:id>", views.author),
    path("recipe/<int:id>", views.recipe),
    

    # path('admin/', admin.site.urls),
]