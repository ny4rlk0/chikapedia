#!/usr/bin/python
#coding=utf-8
import os,sys,warnings,requests,time,urllib,threading
import wikipedia as wiki
from PIL import Image
from io import BytesIO
from locale import getdefaultlocale
warnings.filterwarnings('ignore')
try:
    langue=getdefaultlocale()
    langue=langue[0]
    langue=langue.split("_")
    l=str(langue[0])
except:
    print("Chikapedia failed to get your computer's Langue.")
    print("Switching bacc default langue which is English.")
    l="en"
wiki.set_lang(l)
try:
    if l=="tr":
        l_wiki="Wikide ara: "
        l_how_many="Kaç sonuç: "
        l_search="Ara: "
        l_learn_more="Resim görmek ve daha fazla öğrenmek istermisin? (E/H)"
    else:
        l_wiki="wiki: "
        l_how_many="How Many results you want to see: "
        l_search="Search: "
        l_learn_more="Would you like to see pictures and learn more? (Y/N)"
except:
    os._exit(1)
def k():
    print("-------------------------------------------")
def x():
   try:
    if l=="tr":
        clear()
        print("Yes my Lord!")
        feed=str(input(l_wiki))
        result=int(input(l_how_many))
        k()
        v=wiki.search(feed,results=result)
        n=0
        for s in v:
            print(f"{v[n]}")
            n+=1
        k()
        ara=str(input(l_search))
        k()
        a=wiki.summary(ara, auto_suggest=True, redirect=True)
        print(f"{a}")
        k()
        ans=str(input(l_learn_more))
        ans=ans.lower()
        if ans=="quit":
            os._exit(1)
        if ans.startswith("y") or ans.startswith("e"):
            s=wiki.WikipediaPage(title=ara,redirect=True,preload=True)
            cont=s.content
            imgs=s.images
            print(cont)
            img_num=0
            for i in imgs:
               try:
                url=imgs[img_num]
                #urllib.request.urlretrieve(url, f"{img_num}.jpg")#For Downloading Pictures to same directory uncomment to activate.
                img_num+=1
                time.sleep(1)
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
                img.show()
               except:
                   time.sleep(1)
                   continue
   except:
       pass
def clear():
    if os.name=='nt':
        _=os.system('cls')
    else:
        _=os.system('clear')
#x()
if __name__ == "__main__":
    threading.Thread(target=x).start()