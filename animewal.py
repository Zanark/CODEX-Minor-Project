import wget
import requests
import random
from bs4 import BeautifulSoup


def get_the_image(img_url, USERNAME):
    src_code = requests.get(img_url).text
    soop = BeautifulSoup(src_code , "html.parser")

    for pic in soop.findAll('img', {'id': 'wallpaper'}):
        url = 'https:' + pic.get('src')
        r = requests.get(url)
        with open("/home/$" + USERNAME + "/images/grub.jpg", "wb") as photu:
            photu.write(r.content)




def anime_wallpaper(url , user):
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, "html.parser")

    for imag in soup.findAll( 'a' , { 'class' : 'preview'}):
        img = imag.get('href')
        a = random.randint(1,11)
        if a % 3 == 0:
            get_the_image(img , user)
        else:
            continue


anime_wallpaper("https://alpha.wallhaven.cc/search?q=anime&search_image=&page=2" , "Zanark")
