import json
from django.http import HttpResponse, JsonResponse
from .models import Product

# Create your views here.
def home(request):
    return HttpResponse('<h1>salom</h1>')

def add(request):
    p = request.POST
    db = Product(name=p.get("name"), company=p.get('company'), color=p.get('color'), RAM=p.get('RAM'), memory=p.get('memory'), price=p.get('price'), img_url=p.get('img_url'))
    db.save()
    return JsonResponse({})
