from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .serializers import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Posts
from .forms import PostBasedForm, PostCreateForm, PostDetailForm

from rest_framework import generics

# 게시글 목록
class PostListView(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostListModelSerializer

# 게시글 상세
class PostRetrieveView(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostRetrieveModelSerializer

# 게시글 목록
class PostListCreateView(generics.ListAPIView, generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# 게시글 상세, 수정, 삭제
class PostRetrieveUpdateView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostRetrieveSerializer

class PostModelViewSet(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostListModelSerializer

    #@action(detail=True, methods=['get'])
    #def get_comment_all(self, request, pk=None):
    #    post = self.get_object()
    #    comment_all = post.set_comment.objects.all()
    #    return Response()

# class CommentModelViewSet(ModelViewSet):
#     queryset=Comment.objects.all()
#     serializer_class=CommentHyperlinkedModelSerializer
    



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def index(request):
    post_list = Post.objects.all().order_by('-created_at') # Post 모델에 있는 객체 전부 불러오기
    context = {
        'post_list': post_list,
    }
    return render(request, 'index.html', context)

def post_list_view(request):
    # post_list = Post.objects.all() #Post 모델에 있는 객체 전부 불러오기
    post_list = Post.objects.filter(writer=request.user)
    context = { # Post 객체를 리스트 형태로 담기
        'post_list': post_list,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist: # 존재하지 않는 게시글을 조회할 경우
        return redirect('index') # index.html로 리다이렉트
    post = Post.objects.get(id=id)
    context = {
        'post':post,
        'form' : PostDetailForm(),
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        Post.objects.create( # image, content 데이터를 담은 Post 객체 만들어서 저장
            image = image,
            content = content,
            writer = request.user
        )
        return redirect('index')
# GET은 처음 생성 페이지 들어갔을 때 -> post_form.html 보여주기
# else는 사용자가 폼을 작성하고 제출 버튼을 눌렀을 때 index 페이지 리다이렉트

def post_created_form_view(request):
    if request.method=="GET":
        form = PostCreateForm()
        context = {'form': form}
        return render(request, 'posts/post_form2.html', context)
    else:
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create( #image, content 데이터를 담은 Post 객체 만들어서 저장
            image=form.cleaned_data['image'],
            content=form.cleaned_data['content'],
            writer=request.user
            )
        else:
            return redirect('post:post-create')
        return redirect('index')

    
        return redirect('index')

@login_required
def post_update_view(request, id):

    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id, writer=request.user)

    if request.method == 'GET':
        context = { 'post':post }
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        print(new_image)
        print(content)
        if new_image:
            post.image.delete()
            post.image = new_image

        post.image = new_image
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)

@login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    # post = get_object_or_404(Post, id=id, writer=request.user)
    if request.user != post.writer:
        raise Http404('잘못된 접근입니다.')
    
    if request.method == "GET":
        context = { 'post': post }
        return render(request, 'posts/post_confirm_delete.html',context)
    else:
        post.delete()
        return redirect('index')
    
    

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'

def url_view(request):
    data = {'code': '001', 'msg': 'OK'}
    return HttpResponse('<h1>url_views</h1>')

def url_parameter_view(request, username):
    print(f'url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')

    if request.method == "GET":
        print(f'request.GET: {request.GET}')
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}')
    return render(request, 'view.html')