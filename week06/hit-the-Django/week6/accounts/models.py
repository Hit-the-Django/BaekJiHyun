from django.db import models
from django.shortcuts import render
from .forms import UserCreateForm

def signup_view(request):
    # Get 요청 시 HTML 응답
    if request.method == 'GET':
        form = UserCreateForm
        context = { 'form': form }
        return render(request, 'accounts/signup.html', context)
    else:
        pass

# Create your models here.
