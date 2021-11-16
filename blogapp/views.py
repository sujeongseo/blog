from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

def home(request):
    # 블로그 글들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('date')
    return render(request, 'blogapp/blog.html', {'posts':posts})

#블로그 글 작성 HTMl을 보여주는 함수
def new(request):
    return render(request, 'blogapp/new.html')

#블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

#django form을 이용해서 입력값을 받는 함수
#GET 요청과 (= 입력값을 받을 수 있는 Html을 갖다 줘야함)
#POST 요청 (= 입력한 내용을 데이터 베이스에 저장. form에서 입력한 내용을 처리)
#둘 다 처리가 가능한 함수
def formcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title'] 
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    #     입력 내용을 DB에 저장
    else:
    #     #입력을 받을 수 있는 Html을 갖다 주기
        form = BlogForm()
    return render(request, 'blogapp/form_create.html', {'form':form})


def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'blogapp/form_create.html', {'form':form})


def detail(request, blog_id):
    # blog_id  번째 블로그 글을 Detail.html로 띄워주는 코드
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogapp/detail.html', {'blog_detail':blog_detail})