#This Python script downloaded raster data file in .nc format from specified url


import requests
from bs4 import BeautifulSoup as bs

try:
    resp = requests.get("https://mailtrack.io/trace/link/cb91e92af171a0e317b132507bc57eb22066b02b?url=http%3A%2F%2Ffizz.phys.dal.ca%2F~atmos%2Fmartin%2F%3Fpage_id%3D140&userId=3966469&signature=25076cae96d597e1")
    soup = bs(resp.text,"html.parser")
    p_tags = soup.find_all('p')
    for data in p_tags:
        if "Satellite-Derived PM<sub>2.5</sub>, 2016, at 35% RH [ug/m3]" in str(data):
            temp = data
    temp = temp.find_all('a')
    # print(temp)
    for data in temp:
        if "[.nc]" in str(data):
            x = data
            break

    downloadUrl = x.get('href')
    resp = requests.get(downloadUrl)
    with open("raster.nc","wb") as f:
        f.write(resp.content)
except:
    print("NetworkError or problem with the URL\n")
    
