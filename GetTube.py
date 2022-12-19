""" 
You just put the url of youtube video, choose quality and select 
a name for file then the code executes and the given video downloaded.

Check out this article if you can't figure out what is happening:
https://subhadip.ca/information-technology/scraping-youtube-with-beautifulsoup-and-python3/

I also would like to admit that i haven't put some if-else and try-except 
statements to handle possible errors. If you want to use this code you can simply add them.
"""


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
    
# The below code is up to you, you can modify it anyway you want, and add some conditions to handle errors

GetTube(
    input('URL: '),
    int(input( 'For desired quality choose a number\nHigh:\t0\nMed:\t2\nLow:\t4\n')), 
    input("Type in desired file name (don't add extension): ")
    ).download()
