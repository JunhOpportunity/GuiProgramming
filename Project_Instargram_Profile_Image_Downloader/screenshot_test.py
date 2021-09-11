from urllib import request
from urllib.request import urlopen
from urllib.parse import quote_plus
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from PIL import Image


# 브라우저를 열지 않고 작업 수행하기
# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("window-size=1920x1080")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
# URL 입력. 이제 실제 FUNCTION 파일에서 사용할 때는 format을 이용해야겠디
url = "https://www.naver.com/"
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome(options=options)
next_url = "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s150x150/181971810_800944510823488_6711971698270256080_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=VN8hozkeQG4AX8NYRYU&edm=ABfd0MgBAAAA&ccb=7-4&oh=064e1a116dc298a7c23d50835c5c9c75&oe=6142C5A0&_nc_sid=7bff83"
browser.get(url)
time.sleep(2)
browser.get(next_url)
time.sleep(2)

browser.get_screenshot_as_file("screenshottest.png")

browser.close()

# 스크린샷으로 하니까 png 정상 출력 된다.
# -> 따라서, 프로필 이미지 url 가져온 뒤, 그 url로 접속 후 time.sleep(2)
# 페이지 완전히 바뀌면 스크린샷, 이미지 수정 함수를 통해 가운데만 잘라내기 (150x150)

time.sleep(3)



img_modify = Image.open("screenshottest.png")
print(img_modify.size)
cropped_img = img_modify.crop((885, 465, 1035, 615))
cropped_img.show()

# 스크린 샷 자르는데 문제가 발생했었다.
# crop() takes from 1 to 2 positional arguments but 5 were given
# 라는 오류가 뜨면서 사진을 원하는 크기로 자를 수 없었다.
# 1시간동안 찾고 찾은 끝에 해결하였다.