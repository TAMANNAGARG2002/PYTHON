from django.urls import path
from .import views
urlpatterns = [
    path('category/',views.category),
    path('female/',views.female),
    path('index/',views.index),
    path('kids/',views.kids),
    path('men/',views.men),
    

]
