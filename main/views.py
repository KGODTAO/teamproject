from django.db.models import Q
from django.shortcuts import render
from django.views import View
from main.models import *


class IndexPageView(View):
    def get(self, request):
        categories = Category.object.all()
        return render(request, 'index.html', {'categories': categories})


class IndexPageView(View):
    def get(self, request):
        categories = Category.objects.all()
        posts = Book.objects.all()
        return render(request, 'index.html', locals())


