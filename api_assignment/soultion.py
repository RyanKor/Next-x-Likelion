import requests, json, xmltodict

apiKey = 'http://apis.data.go.kr/1400119/service/rest/KfniService/btncSearch?ServiceKey=FkQER%2BXH5fEOw1bzIOREseme8QEGHD09o0wQjlLw6Tzj6r7EsxXMovrWQt5iUSY5v6xolwZhGTqwToqCLYsk%2Fw%3D%3D&st=1&sw=잠자리'
raw_data = requests.get(apiKey).content

xmlObject = xmltodict.parse(raw_data)
dataShown = xmlObject['response']['body']['items']['item']

print(type(raw_data))
# print(xmlObject)

info = []
for data in dataShown:
    info.append({'insctSpecsScnm': data['insctSpecsScnm'],
        'insctGnrlNm' : data['insctGnrlNm']})
    
    print("해당 곤충의 영문 학명은 " + data['insctSpecsScnm'] + "으로 국문 명칭은 ")
    print(data['insctGnrlNm'] + " 이라 합니다.")
    print("----------------------------------")