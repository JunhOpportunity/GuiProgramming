import requests
from bs4 import BeautifulSoup
import time
# fucntion

# URL
# def go_url():
#     pass
# url = "https://www.instagram.com/aespa_official/"
# # url = "{}".format(url_entry.get())
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# profile_image = soup.find("img", attrs={"class":"_6q-tv"})

# image_url = profile_image["src"]
# image_res = requests.get(image_url)
# image_res.raise_for_status()

# with open("testimage.png", "wb") as f:
#     f.write(image_res.content)

#
url = "https://www.instagram.com/aespa_official/feed"
res = requests.get(url, headers=headers)    # 이걸 해줘야 사용자 입장에서 접속하는 것으로 보이게 할 수 있다고 나는 그렇게 이해함
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
images = soup.find("img")

image_res = requests.get(images["src"])
image_res.raise_for_status()
with open("moive.jpg", "wb") as f:    # {}를 하나만 쓰면, 년도가 변경될 때 마다 파일 이름이 중복되므로 덮어쓰기 된다. 따라서 year를 나타내는 {}까지 총 두 개를 써준다
    f.write(image_res.content)