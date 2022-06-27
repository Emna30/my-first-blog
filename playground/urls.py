#from operator import imod
#from django.urls import URLPattern, path
#from .import views 

#URL config
#URLPatterns = [
 #   path('hello/', views.say_hello.urls),
#]

from django.urls import path
from . import views 

urlpatterns = [
    path ('',views.post_list, name ='post_list'),

    ]