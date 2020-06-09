from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def category_list(request):
    category = Category.objects.all()
    context = {
        'category_list': category
    }
    return render(request, 'core/index.html', context)