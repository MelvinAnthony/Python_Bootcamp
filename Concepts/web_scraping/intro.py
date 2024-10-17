import requests
import bs4

#using requests package to get the raw data from source
result = requests.get("https://en.wikipedia.org/wiki/Cricket")
#print(result.text)

#using bs4 and lxml to align the data into format.
soup = bs4.BeautifulSoup(result.text,'lxml')
#print(soup)

#using tag filter the data
#print(soup.select('title'))

#filter using li
# site_li = soup.select('li')
# print(site_li[1].get_text())


#using class operation 

# for item in soup.select(".wikitable"):
    # print(item.text)

# scraping image

# image_scrap = soup.select(".mw-file-description img")
# first_image = image_scrap[0]
# print(first_image['src'])

#using tag
image_tag = '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Pollock_to_Hussey.jpg/300px-Pollock_to_Hussey.jpg">'
soup = bs4.BeautifulSoup(image_tag,'html.parser')
image_tag = soup.find('img')
print(image_tag['src'])