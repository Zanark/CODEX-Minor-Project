import requests
import random
from bs4 import BeautifulSoup


print("\n\n This is the Web Scraper for the website https://alpha.wallhaven.cc and the downloaded image will be used as bootloader wallpaper")
username   = input("\n\n Enter the USERNAME ")
search_tag = input("\n\n Enter the Tag realted to the wallpaper you wish to download")



def get_the_image(img_url, USERNAME):
    src_code = requests.get(img_url).text
    soop = BeautifulSoup(src_code , "html.parser")

    for pic in soop.findAll('img', {'id': 'wallpaper'}):
        url = 'https:' + pic.get('src')
        r = requests.get(url)
        with open("/home/$" + USERNAME + "/images/grub.jpg", "wb") as photu:
            photu.write(r.content)


def wallpapa(tag , user):
    
    url = "https://alpha.wallhaven.cc/search?q=" + tag + "&search_image="
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, "html.parser")

    for imag in soup.findAll( 'a' , { 'class' : 'preview'}):
        img = imag.get('href')
        a = random.randint(1,11)
        if a % 3 == 0:
            get_the_image(img , user)
        else:
            continue


wallpapa(search_tag, username)
                
