# pandas 라이브러리 가져오기
import pandas as pd

# HTML 코드를 파이썬에 불러오는 역할
import requests

# HTML 코드의 원하는 정보를 크롤링하는 역할
from bs4 import BeautifulSoup

# 환율 URL
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%ED%99%98%EC%9C%A8"
#url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8%EC%A1%B0%ED%9A%8C"

# 환율 HTML 코드
get_page = requests.get(url)

# 텍스트 파일로 저장
exchange_rate = get_page.text

# BeautifulSoup의 html.parser에 적용
soup = BeautifulSoup(exchange_rate, 'html.parser')

# 원하는 정보의 html상 위치
ex_tables = soup.select('.tbl_rwd > tbody > tr')
ex_index = soup.select('.tbl_rwd > tbody > tr > td > a')
#print(ex_index)

# 주된 내용
tables = []
for ex in ex_tables:
    tables.append(ex.text)
#print(tables)

#index 정보
main_index = []
for ex in ex_index:
    main_index.append(ex.text)
#print(main_index)


# 리스트 나누기 (List comprehension 활용)
n = 4
result = [tables[i * n:(i + 1) * n] for i in range((len(tables) + n - 1) // n )]

# 판다스(Pandas)를 통하여 데이터 프레임(DataFrame) 만들기
df = pd.DataFrame(data = result, index = main_index)
df
