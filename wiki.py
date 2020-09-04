#!/usr/bin/python
#coding=utf-8
import os,sys,warnings,requests,time,urllib,threading,csv
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
        l_num="Numara gir: "
        l_learn_more="Resim görmek ve daha fazla öğrenmek istermisin? (E/H)"
        l_exit=f"Çıkmak için küçük harfle çık.\nProgramı yeniden çalıştırmak için herhangi bişey yazın:\n"
    else:
        l_wiki="wiki: "
        l_how_many="How Many results you want to see: "
        l_search="Search: "
        l_num="Enter a number: "
        l_learn_more="Would you like to see pictures and learn more? (Y/N)"
        l_exit=f"Type quit to exit or anything else to restart the program\n:"
except:
    os._exit(1)
def k():
    print("-------------------------------------------")
def x():
   try:
    while True:
        clear()
        print("Yes my Lord!")
        feed=str(input(l_wiki))
        if feed=="quit" or feed=="çıkış" or feed=="exit" or feed=="q" or feed=="çık":
            os._exit(1)
        result=int(input(l_how_many))
        k()
        v=wiki.search(feed,results=result)
        n=0
        for s in v:
            #print(f"  {v[n]}")# 1-) XXXXXXXX
            print('['+str(n)+']''-'+v[n])
            n+=1
        k()
        n_index=int(input(l_num))
        target_info=v[int(n_index)]
        #ara=str(input(l_search))
        k()
        new_info=wiki.summary(target_info, auto_suggest=True, redirect=True)
        print(f"{new_info}")
        k()
        ans=str(input(l_learn_more))
        ans=ans.lower()
        if ans.startswith("y") or ans.startswith("e"):
            clear()
            s=wiki.WikipediaPage(title=target_info,redirect=True,preload=True)
            cont=s.content
            imgs=s.images
            print(cont)
            with open("Last Article.txt","w",encoding='UTF-8') as f:#Write content to file
                w = csv.writer(f,delimiter=",",lineterminator="\n")
                w.writerow([cont])
            img_num=0
            for i in imgs:
               try:
                url=imgs[img_num]
                urllib.request.urlretrieve(url, f"Last Article Picture {img_num}.jpg")#For Downloading Pictures to same directory uncomment to activate.
                img_num+=1
                time.sleep(1)
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
                img.show()
               except:
                   time.sleep(1)
                   continue
        stat=input(l_exit)
        if stat=="quit" or stat=="çık":
            os._exit(1)
        else:
            continue
   except:
       pass
def clear():
    if os.name=='nt':
        _=os.system('cls')
    else:
        _=os.system('clear')
if __name__ == "__main__":
    threading.Thread(target=x).start()