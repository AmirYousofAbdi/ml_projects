import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


global names
names = []


def count_page(addr = 'https://boardgaming.com/category/games/board-games'):
    res = requests.get(addr)
    soup = bs(res.text,'html.parser')
    soup = soup.find('div',attrs={'class':'pagination'})
    soup = soup.find('span')
    num = str(soup.text)
    index = num.find('f')
    num = num[index+2:]
    try:
        return int(num)
    except:
        return 205

def prep_link(link):

    link = str(link)
    l = link.find('"')
    link = link[l + 1:]
    r = link.find('"')
    link = link[:r]

    return link

def find_page(addr = 'https://boardgaming.com/category/games/board-games'):
    res = requests.get(addr)
    soup = bs(res.text,'html.parser')
    soup = soup.find('div',attrs={'id':'pagination'})
    print(soup.text)


def page_crawling(addr):
    res = requests.get(url=addr)

    soup = bs(res.text ,'html.parser')
    soup = soup.find('div' ,attrs={'class' :'teasers'})

    links = soup.find_all('a')

    # for i in links:
    #   print(i)

    for i in range(0 ,len(links) ,4):

        link = prep_link(links[i])

        try:
            if  not '#' in link:
    
                res = requests.get(url=link)
    
                soup = bs(res.text, 'html.parser').find('div', attrs={'id': 'container'})
                name = soup.find('div', attrs={'id':'title-area'})
    
                name.append(name)
    
                print(name.text)
        except:
            pass
        '''
        if not '#' in link:
            res = requests.get(url=link)

            soup = bs(res.text, 'html.parser').find('div', attrs={'id': 'container'})
            name = soup.find('div', attrs={'id': 'title-area'})

            names.append(name)
            print(name)'''
        print(1)

for i in range(1,count_page()+1):
    addr = f'https://boardgaming.com/category/games/board-games/page/{i}'
    page_crawling(addr)


df = {'name' : names}


df = pd.DataFrame(df)
#df.to_csv('data.csv',index=True,mode='w')
df.to_csv('data.txt',index=True,mode='w',sep=',')
