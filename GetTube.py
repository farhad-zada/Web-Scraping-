import requests as rs
from bs4 import BeautifulSoup as bs
import json as js

class GetTube:
  def __init__(self, url, quality, file_name) -> None:
    self.url = url
    self.quality = quality
    self.fname = file_name

  def download(self):
    content = rs.get(js.loads(bs(rs.get(self.url).content, 'html.parser').find('body').find('script').string[30:-1])['streamingData']['adaptiveFormats'][self.quality]['url'], stream = True)
    fhand = open(self.fname + ".mp4", 'wb')
    [fhand.write(chunk) for chunk in content.iter_content(chunk_size = 1024**2) if chunk]
    fhand.close()

GetTube(
    input('URL: '),
    int(input( 'For desired quality choose a number\nHigh:\t0\nMed:\t2\nLow:\t4\n')), 
    input("Type in desired file name (don't add extension): ")
    ).download()


# Used : 
'https://subhadip.ca/information-technology/scraping-youtube-with-beautifulsoup-and-python3/'