from django.shortcuts import render, redirect
from .forms import ContentsForm, CommentForm
from .models import WritingContents, Comment

# Create your views here.
def home(request):
    posts = WritingContents.objects.all()
    return render(request, 'home.html', {'posts': posts})
# home.html을 추가하면 url에 쏘아줄 함수를 여기서 추가한다.
def create(request):
    if request.method == 'POST':
        #이 부분이 글을 Post 형태로 Url에 쏴주는 것임.
        form = ContentsForm(request.POST)
        post = form.save(commit=False)
        form.save()
        return redirect('postDetail', post.pk)
    else:
        form = ContentsForm()
    return render(request, 'create.html', {'form': form})
# create.html을 추가하면 마찬가지로 view.py에서 기능을 추가해야함

def postDetail(request, post_pk):
    if request.method == 'POST':
        post = WritingContents.objects.get(pk = post_pk)
        form = CommentForm(request.POST)
        comment = form.save(commit = False)
        comment.post = post
        comment.save()
        return redirect('postDetail', post.pk)
    else:
        post = WritingContents.objects.get(pk=post_pk)
        form = CommentForm()
        return render(request, 'postDetail.html', {'post' : post, 'form' : form})
# postDetail.html은 게시글 생성이후 글을 읽기 위한 페이지다.

def comment_delete (request, post_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)

    comment.delete()

    return redirect('postDetail', post_pk)

# edit.html을 추가했기 때문에 여기서 view.py에 반드시 html에서
# 기능이 작동할 수 있는 함수를 추가해줘야만한다.

def edit(request, post_pk):
    post = WritingContents.objects.get(pk = post_pk)
    if request.method == 'POST':
        form = ContentsForm(request.POST,instance = post)
        form.save()
        return redirect('postDetail', post.pk)
    else:
        form = ContentsForm(instance = post)
    return render(request, 'edit.html', {'form': form})

def delete(request, post_pk):
    post = WritingContents.objects.get(pk = post_pk)
    post.delete()
    return redirect('home')
    
