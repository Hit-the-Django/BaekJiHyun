from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
  return render(request, 'index.html')

def intro(request):
  return render(request, 'intro.html')

def market(request):
  posts = Post.objects.order_by('price') 
  return render(request, 'market.html', {'posts': posts})

def post_detail(request, pk): 
  post = Post.objects.get(pk=pk)
  return render(request, 'post_detail.html',{'post': post})

def post_new(request):
    if request.method == "POST":
      form = PostForm(request.POST)
      if form.is_valid():
        post = form.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
