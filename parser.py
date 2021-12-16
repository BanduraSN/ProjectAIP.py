import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.kinoafisha.info/rating/movies/action/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.61 (Edition Yx GX)'
}

results=[]

req = requests.get(url, headers=headers)

src=req.text

soup = BeautifulSoup(src, 'lxml')

all_f=soup.find_all(class_='movieItem_info')

for film in all_f:
    namef= film.find(class_='movieItem_title').text
    yearf= film.find(class_='movieItem_year').text[:4]
    ratef= film.find(class_='rating_num').text
    #print(namef,yearf,ratef)
    results.append({
        'Название':namef,
        'Год': yearf,
        'Рейтинг': ratef
    })

Newurl = url+'?page='

for i in range(1,8):
    Url=Newurl+str(i)

    req=requests.get(Url,headers= headers)

    src= req.text

    soup = BeautifulSoup(src,'lxml')

    AllFilms = soup.find_all(class_='movieItem_info')

    for item in AllFilms:
        namef = item.find(class_='movieItem_title').text
        yearf = item.find(class_='movieItem_year').text[:4]
        ratef = item.find(class_='rating_num').text
        print(namef,yearf,ratef)
        results.append({
            'Название': namef,
            'Год': yearf,
            'Рейтинг': ratef
        })

namep=url[42:-1]

with open(f'Films/{namep}.json', 'w', encoding='utf-8-sig') as file:
    json.dump(results,file,indent=4,ensure_ascii=False)