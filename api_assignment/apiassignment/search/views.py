from django.shortcuts import render,redirect
import requests, json, xmltodict

# Create your views here.

def home(request):
    apiKey = 'http://apis.data.go.kr/1400119/service/rest/KfniService/btncSearch?ServiceKey=키값&st=1&sw=잠자리'
    raw_data = requests.get(apiKey).content

    xmlObject = xmltodict.parse(raw_data)
    dataShown = xmlObject['response']['body']['items']['item']
    print(type(raw_data))
    info = []
    for data in dataShown:
        info.append({'insctSpecsScnm': data['insctSpecsScnm'],'insctGnrlNm' : data['insctGnrlNm'],'cprtCtnt' : data['cprtCtnt']})
    
    return render(request, 'home.html', {'dataShown': info})