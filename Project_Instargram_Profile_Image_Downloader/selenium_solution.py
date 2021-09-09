from urllib.request import urlopen
from urllib.parse import quote_plus
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 브라우저를 열지 않고 작업 수행하기
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")

# URL 입력. 이제 실제 FUNCTION 파일에서 사용할 때는 format을 이용해야겠디
url = "https://www.instagram.com/aespa_official/"
browser = webdriver.Chrome(options=options)
browser.get(url)

time.sleep(4)

html = browser.page_source
soup = BeautifulSoup(html)

time.sleep(4)

# class 검색 후 src 뒤의 text 가져오기
insta = soup.select_one('._6q-tv')
img_url = insta["src"]
print(img_url)

# 사진 저장하기
with urlopen(img_url) as f:
    with open("testImg.jpg", "wb") as h:
        img = f.read()
        h.write(img)

browser.close()

# emergency resolved!!!!!!!!!!!!!!!!!!!!!!!!!!!