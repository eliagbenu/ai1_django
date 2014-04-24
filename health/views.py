from django.shortcuts import render

# Create your views here.

def traditional(request):
    return render(request,'health.html')

def hospital(request):
    return render(request,'health.html')


def pharmacy(request):
    return render(request,'health.html')


def chemist(request):
    return render(request,'health.html')

