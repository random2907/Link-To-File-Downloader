from __future__ import unicode_literals
import yt_dlp
import subprocess
import wget
import gdown
txt=open('text.txt','r')

x=txt.readlines()
num = sum(1 for line in open('text.txt'))
print(num)
n=0
try:
    for i in range(num):
        z=x[n]
        z=z.strip()
        y=z.split('/')
        if y[2]=="drive.google.com":
            print('drive link : ',z)
            gdown.download(z,fuzzy=True)
            n+=1
        elif y[2]=='www.youtube.com' or y[2]=='youtu.be':
            print('youtube link : ',z) 
            ydl_opts = {}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([z])
            n+=1
        elif y[2]!='www.youtube.com' or y[2]!='youtu.be' and y[2]!='drive.google.com':
            print('direct link :',z)
            wget.download(z)
            n+=1    
        
except IndexError:
    print('Done') 



      
    
    

