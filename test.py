import requests
from bs4 import BeautifulSoup

def show_info():
    code_receive = '035720'

    url = 'https://finance.naver.com/item/main.nhn?code=' + code_receive

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    # chart_area > div.rate_info > div > p.no_today
    # chart_area > div.rate_info > div > p.no_today

    # tab_con1 > div.first > table > tbody > tr.strong > td
    # _per

    주가 = soup.select_one('#chart_area > div.rate_info > div > p.no_today')
    시총 = soup.select_one('#tab_con1 > div.first > table > tbody > tr.strong > td')
    PER = soup.select_one('#_per')

    print(주가, 시총, PER)