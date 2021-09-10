from urllib import request
from urllib.request import urlopen
from urllib.parse import quote_plus
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time


# 브라우저를 열지 않고 작업 수행하기
# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("window-size=1920x1080")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")

# URL 입력. 이제 실제 FUNCTION 파일에서 사용할 때는 format을 이용해야겠디
url = "https://www.naver.com/"
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
next_url = "https://www.instagram.com/aespa_official/feed"
browser.get(url)
time.sleep(2)
browser.get(next_url)
time.sleep(2)

browser.get_screenshot_as_file("screenshottest.png")

browser.close()

# 스크린샷으로 하니까 png 정상 출력 된다.
# -> 따라서, 프로필 이미지 url 가져온 뒤, 그 url로 접속 후 time.sleep(2)
# 페이지 완전히 바뀌면 스크린샷, 이미지 수정 함수를 통해 가운데만 잘라내기 (150x150)