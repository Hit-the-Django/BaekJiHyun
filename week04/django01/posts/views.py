from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView
from .models import Post

def url_view(request):
    return HttpResponse('url.view')

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'

# Create your views here.
