import sys
from BeautifulSoup import BeautifulSoup
import urllib2
import urllib

def translate(src, des, text):
    data = {'sl':src,'tl':des,'text':text}
    querystring = urllib.urlencode(data)
    request = urllib2.Request('http://www.translate.google.com' + '?' + querystring)

    request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')
    opener = urllib2.build_opener()
    feeddata = opener.open(request).read()
    soup = BeautifulSoup(feeddata)
    return soup.find('span', id="result_box").getText()
