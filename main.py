from download import direct
import multiprocessing
import uuid

def main(url):
    try:
        direct(url,str(uuid.uuid4))
    except Exception as err:
        print(f"error {err=},{type(err)=}")


url=[]
print("x to start download")
while True:
    x=input(f"{len(url)+1}. Enter url : ")
    if x=="x":
        break
    url.append(x)
    
with multiprocessing.Pool(processes=len(url)) as pool:
    data=pool.map(main,url)
    
    
            

