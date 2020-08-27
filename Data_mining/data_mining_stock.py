import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

res = rq.post("http://tsetmc.com/tsev2/data/instinfofast.aspx?i=46348559193224090&c=27%20",
              params={'Accept':'text/plain, */*; q=0.01',
                      'Accept-Encoding':'gzip, deflate',
                      'Accept-Language':'en-US,en;q=0.9',
                      'Connection':'keep-alive',
                      'Cookie':'ASP.NET_SessionId=mu4oqfpblxfcpyl5hv41dss4; _ga=GA1.2.1672943417.1598547869; _gid=GA1.2.1380555790.1598547869',
                      'Host':'tsetmc.com',
                      'Referer':'http://tsetmc.com/Loader.aspx?ParTree=151311&i=46348559193224090',
                      'User-Agent':'ozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
                      'X-Requested-With':'XMLHttpRequest'})

print(res.text)