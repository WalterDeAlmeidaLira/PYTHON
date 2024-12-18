from django.shortcuts import render,HttpResponse

def cars(request):
    return HttpResponse("carros")
