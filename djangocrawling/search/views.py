from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

# Create your views here.


def home(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
        search_word = url + word
        data = requests.get(search_word).text
        soup = BeautifulSoup(data, 'html.parser')
        titles = soup.find_all(class_='_sp_each_title')
        title_list = []
        for title in titles:
            title_list.append({
                'url':title.get('href'),
                'title':title.get('title')
            })
        return render(request, 'result.html', {'title_list':title_list})
    else:
        return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')
