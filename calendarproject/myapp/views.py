from django.shortcuts import render
from django.http import HttpResponse
# Create your views heredef 
def index(req):
  return render(req, 'myapp/index.html')



def whatthefuck(req):
    return HttpResponse('Sus Tan')