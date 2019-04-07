from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
# 홈 화면에 request받으면 페이지 띄우기

def result (request):
    text = request.GET['fulltext']
    textcount = len(text)
    divide = text.split() #알아서 쪼개진 단어들이 리스트 형태로 출력된다.
    dic = {}
    for ch in divide:
        if ch in dic:
            dic[ch] +=1
        else:
            dic[ch] = 1
    return render(request, 'result.html', {'text' : text, 'textcount' : textcount, 'dic': dic, 'divide': divide,'ch': ch,})