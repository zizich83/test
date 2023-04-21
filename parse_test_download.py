import requests
import fake_useragent
from bs4 import BeautifulSoup

storage_number = 1
image_number = 0
link = f"https://zastavok.net"

for storage in range(2):
    response = requests.get(f'{link}/{storage_number}').text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', class_ = 'block-photo')
    all_image = block.find_all('div', class_ = 'short')
    #print(all_image)
    for image in all_image:
        #print(image)
        image_link = image.find('a').get('href')
        download_storage = requests.get(f'{link}{image_link}').text
        downlaod_soup = BeautifulSoup(download_storage, 'lxml')
        download_block = downlaod_soup.find('div', class_ = 'image_data').find('div', class_ = 'block_down')
        result_link = download_block.find('a').get('href')

        # Download image
        image_bytes = requests.get(f'{link}{result_link}').content

        with open(f'image/{image_number}.jpg', 'wb') as file:
            file.write(image_bytes)
        image_number += 1
        print(f'Image {image_number}.jpg success download')

    storage_number += 1