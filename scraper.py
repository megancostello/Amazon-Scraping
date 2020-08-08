import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

workbook = load_workbook(filename="Log.xlsx")
sheet = workbook["Logged"]

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
urls = ["https://www.amazon.com/dp/B005VS9WO6", "https://www.amazon.com/dp/B0081XINMA", "https://www.amazon.com/dp/B0711Y9Y8W",
        "https://www.amazon.com/dp/B00FPKNRG4", "https://www.amazon.com/dp/B075FY228K"]
rowCounter = 2

def getData(pageURL):
    response = requests.get(pageURL, headers=headers1)
    soupy = BeautifulSoup(response.content, 'html.parser')
    return soupy

for url in urls:
    soup = getData(url)
    title = ''
    try:
        title = soup.find(id="productTitle").get_text().rstrip()
        print('soup is good')
    except AttributeError:
        soup = getData(url)
        print('soup redone')
        title = soup.find(id="productTitle").get_text().rstrip()
    brand = soup.find(id="bylineInfo").get_text().rstrip()
    #mainImg = soup.find(id="landingImage")
    #altImgs = soup.find_all("li", class_="a-spacing-small item imageThumbnail a-declarative")
    #altImgs = soup.find_all(attrs={"class":"a-spacing-small item imageThumbnail a-declarative"})
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

    sheet.cell(row=rowCounter, column=1).value = title
    sheet.cell(row=rowCounter, column=2).value = brand
    sheet.cell(row=rowCounter, column=3).value = styleCount
    sheet.cell(row=rowCounter, column=4).value = sizeCount
    sheet.cell(row=rowCounter, column=5).value = colorCount

    workbook.save("Log.xlsx")
    rowCounter+=1
#print(response.text)
#print("product: ",title)
#print("brand: ",brand)
#print(mainImg)
#print('Style count: ', styleCount)
#print('Size count: ', sizeCount)
#print('Color count: ', colorCount)
#print(len(altImgs))
