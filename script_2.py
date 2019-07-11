# This is a python script to download shape data file from specified site in .shp format
# Your shapefile will be downloaded.

import requests
from bs4 import BeautifulSoup as bs
import webbrowser

try:
    home_url = "https://sedac.ciesin.columbia.edu"
    resp = requests.get("https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-ext-polygons-rev01/data-download")
    soup = bs(resp.text,"html.parser")
    a_tags = soup.find_all('a')
    for link in a_tags:
        if ".zip" in str(link.get('href')) and "shp" in str(link.get('href')):
            data = link.get('href')
    
    download_url = home_url + str(data)
    resp = requests.get(download_url)
    with open("shape.shp","wb") as f:
        f.write(resp.content)
    
    webbrowser.open("shape.shp")
    
except:
    print("Network error or Problem with the URL")
