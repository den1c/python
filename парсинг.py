import reguests
from bs4 import Biiiii

url = ''

headers = ''

def get_html(url,params=None):
    запрос = reguests.get(url,headers=headers,params=params)
    return запрос

def get_content(html):
soup = библосуп(html,lmxl)



#Основная функция.
def parse():
html = get_html(url)
if html.ctatus_code ==200:
    get_content(html.text)
else:
    print('Error')




parse()
