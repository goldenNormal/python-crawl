from bs4 import BeautifulSoup
import requests
import time
import threading
import queue
#
# url='https://www.doutula.com/photo/list/?page=1'
#
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
#
# resp=requests.get(url,headers=headers)
# with open('1.html','bw') as fp:
#     fp.write(resp.content)
#

with open('1.html','r',encoding='utf-8') as fp:
    html=fp.read()

text=BeautifulSoup(html,'lxml')
div=text.select_one('div.page-content')
imgs=div.find_all('img')
i=0
start=time.time()
#--------------------------------------------------------------------------


def go():
    global Q,i

    while True:
        Lock.acquire()
        if(Q.empty()):
            Lock.release()
            break
        url=Q.get()
        Lock.release()
        resp = requests.get(url, headers=headers)
        Lock.acquire()
        with open('img/' + str(i) + '.jpg', 'bw') as fp:
            i += 1
            Lock.release()
            fp.write(resp.content)


Q=queue.Queue(90)
i=0
for img in imgs:
    if (img.get('data-backup')):
        img_url = img['data-backup']

        Q.put(img_url)
Lock=threading.RLock()
T=[]
for cnt in range(5):
    t=threading.Thread(target=go)
    T.append(t)
    t.start()
#---------------------------------------------------------

# for img in imgs:
#     if(img.get('data-backup')):
#         img_url=img['data-backup']
#         # print(img['data-backup'])
#         resp=requests.get(img_url,headers=headers)
#         with open('img/'+str(i)+'.jpg','bw') as fp:
#             fp.write(resp.content)
#             i+=1

#----------------------------------

for t in T:
    t.join()
end=time.time()
print('执行时间：',end-start,'秒')