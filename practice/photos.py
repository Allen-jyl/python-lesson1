# import requests
# from bs4 import BeautifulSoup
#
# headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/134.0.0.0 " "Safari/537.36 Edg/134.0.0.0" } request = requests.get(
# "https://stock.tuchong.com/search?source=tc_pc_home_search&term=%E7%A7%81%E6%88%BF%E7%85%A7", headers=headers) html
# = request.text soup = BeautifulSoup(html, "html.parser") photos = soup.find_all("a", attrs={"class":
# "search-result-item"}) for photo in photos: print(photo["href"])

import requests
from bs4 import BeautifulSoup
import os
import re


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)


def crawl_images(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    image_items = soup.find_all('div', class_='item')

    for item in image_items:
        image_url = item.find('img')['src']
        # 这里假设通过图片的alt属性获取相册名称，实际情况可能需要调整
        album_name = item.find('img')['alt']
        album_name = re.sub(r'[\\/*?:"<>|]', '', album_name)  # 去除文件名中不允许的字符
        create_folder(album_name)

        image_name = image_url.split('/')[-1]
        save_path = os.path.join(album_name, image_name)
        download_image(image_url, save_path)


if __name__ == "__main__":
    target_url = "https://stock.tuchong.com/search?source=tc_pc_home_search&term=%E7%A7%81%E6%88%BF%E7%85%A7"
    crawl_images(target_url)