from django.shortcuts import render

# Create your views here.


def telcos(request):
    return render(request,'health.html')

def content_providers(request):
    return render(request,'health.html')
