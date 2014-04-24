from django.shortcuts import render

# Create your views here.

def university(request):
    return render(request,'education.html')


def polytechnic(request):
    return render(request,'education.html')


def high_school(request):
    return render(request,'education.html')


def vocational(request):
    return render(request,'education.html')
