from urllib.error import HTTPError
import requests
import yt_dlp
import wget
import gdown
num = int(input("how many links you have = "))
x=[]
for k1 in range (num):
    url =input("enter url = ")
    x.append(url)
n=0    
for i in range(num):      
    try:
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
    except HTTPError:
        r = requests.get(z, allow_redirects=True)
        k=z.split('/')
        open(k[-1], 'wb').write(r.content)
         



      
    
    

