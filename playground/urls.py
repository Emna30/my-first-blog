from operator import imod
from django.urls import URLPattern, path
from .import views 

#URL config
URLPatterns = [
    path('hello/', views.say_hello)
]