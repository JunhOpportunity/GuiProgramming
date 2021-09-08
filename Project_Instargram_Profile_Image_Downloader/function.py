import requests
from bs4 import BeautifulSoup
# fucntion

# URL
# def go_url():
#     pass
url = "https://www.instagram.com/aespa_official/"
# url = "{}".format(url_entry.get())
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
profile_image = soup.find("img", attrs={"class":"_6q-tv"})
image_res = requests.get(profile_image["src"])
image_res.raise_for_status()
print(profile_image)

#-----------------------------------------------------------------
