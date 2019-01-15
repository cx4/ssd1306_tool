# -*— coding:utf-8 -*-
'''author：Roy-Chang
   email：royalive#outlook.com
   https://cx4.tw
'''
from bs4 import BeautifulSoup
import requests
import time
from urllib.parse import quote
def get_model(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text,'lxml')
    time.sleep(2)
    font_model = soup.find_all('p')
    return font_model[3].text
def gen_content(x):
    y = []
    y = x.split(',')
    z1 = ','.join(y[0:16])
    z2 = ','.join(y[16:])
    print(z1 + ",")
    print(z2 + ",")
if __name__ == "__main__":
    content = input("请输内容")
    for i in range(len(content)):
        time.sleep(2)
        print("#文字： "+content[i])
        gen_content(get_model('https://www.eecso.com/test/zimo/?word='+ quote(content[i],encoding='gbk')))