from django.shortcuts import render, redirect
from .forms import ContentsForm
from .models import WritingContents
# Create your views here.
def home(request):
    posts = WritingContents.objects.all()
    return render(request, 'home.html', {'posts': posts})
# home.html을 추가하면 url에 쏘아줄 함수를 여기서 추가한다.
def create(request):
    if request.method == 'POST':
        form = ContentsForm(request.POST)
        post = form.save(commit=False)
        form.save()
        return redirect('postDetail', post.pk)
    else:
        form = ContentsForm()
    return render(request, 'create.html', {'form': form})
# create.html을 추가하면 마찬가지로 view.py에서 기능을 추가해야함

def postDetail(request, post_pk):
    post = WritingContents.objects.get(pk=post_pk)
    return render(request, 'postDetail.html', {'post' : post})
# postDetail.html은 게시글 생성이후 글을 읽기 위한 페이지다.