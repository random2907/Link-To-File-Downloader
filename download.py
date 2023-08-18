#for most download link

import requests as req

def direct(url,filename):
    test=req.get(url)
    with open(filename,"wb") as img:
        img.write(test.content)
    print("download done\nAs {filename}")


    
    
