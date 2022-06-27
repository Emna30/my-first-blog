
#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# request handler 
# request --> response

#def say_hello (request):
   # return HttpResponse('hello world')

def post_list (request):
      return render (request,'playground/post_list.html' , {})
   

