from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest

# Create your views here.
def home(request):
    return JsonResponse({})
