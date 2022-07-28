from bs4 import BeautifulSoup
import urllib.request as urllib
import time

def get_data(url):
  hdr = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  }
  req  = urllib.Request(url, headers=hdr)
  page = urllib.urlopen(req)
  soup = BeautifulSoup(page, 'html.parser')
  list_text = soup.find_all('h2', attrs={'class':'itemTitle'})
  for term in list_text:
    term_text = term.text.strip()
    cs_terms_file.writelines(term_text+'\n')

cs_terms_file = open("cs_terms.txt", "w")

urls = []
for i in range(30, 326):
  get_data(f'https://www.oxfordreference.com/view/10.1093/acref/9780199688975.001.0001/acref-9780199688975?btog=chap&hide=true&page={i}&pageSize=20&skipEditions=true&sort=titlesort&source=%2F10.1093%2Facref%2F9780199688975.001.0001%2Facref-9780199688975')
  time.sleep(2000)

cs_terms_file.close()