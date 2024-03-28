from django.shortcuts import render

# Create your views here.
def database_homepage(request):
    return render(request,'database_homepage.html',{})