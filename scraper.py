import requests
from bs4 import BeautifulSoup

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
url = "https://www.amazon.com/Squirrel-Interactive-Outward-Hound-Ginormous/dp/B005VS9WO6?ref_=ast_sto_dp"

response = requests.get(url, headers=headers1)
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find(id="productTitle").get_text().rstrip()
brand = soup.find(id="bylineInfo").get_text().rstrip()
#mainImg = soup.find(id="landingImage")
#altImgs = soup.find_all("li", class_="a-spacing-small item imageThumbnail a-declarative")
altImgs = soup.find_all(attrs={"class":"a-spacing-small item imageThumbnail a-declarative"})
sample = title
styleCount = 0
baseStyleName = "style_name_"
styleName = baseStyleName + str(styleCount)

while soup.find(id=styleName):
    styleCount+=1
    styleName = baseStyleName + str(styleCount)

sizeCount = 0
baseSizeName = "size_name_"
sizeName = baseSizeName + str(sizeCount)

while soup.find(id=sizeName):
    sizeCount+=1
    sizeName = baseSizeName + str(sizeCount)

colorCount = 0
baseColorName = "color_name_"
colorName = baseColorName + str(colorCount)

while soup.find(id=colorName):
    colorCount+=1
    colorName = baseColorName + str(colorCount)

for char in title:
    if (char == '\n'):
       title = title.replace(char, '')


#print(response.text)
print("product: ",title)
print("brand: ",brand)
#print(mainImg)
print('Style count: ', styleCount)
print('Size count: ', sizeCount)
print('Color count: ', colorCount)
#print(len(altImgs))
