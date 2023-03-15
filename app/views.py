from django.shortcuts import render

# Create your views here.

def oops(request):
    return render(request,'oops.html')

def classs(request):
    return render(request,'classs.html')
