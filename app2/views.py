from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_string(request):
    return HttpResponse('<h1>This is  app2_string page</h1>')
def app2_htmlpage(request):
    return render(request,'app2_htmlpage.html')