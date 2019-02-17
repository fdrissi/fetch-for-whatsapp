from BeautifulSoup import BeautifulSoup
from six.moves import urllib
import urllib2
import re
for i in range(65):
    url = "https://your-site/?page={}".format(i) #change url
    req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urllib2.urlopen(req)
    soup = BeautifulSoup(html_page)
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^https://chat.whatsapp.com")}):
        links.append(link.get('href'))
   	print(links)