#!/usr/bin/env python3

import urllib.request
from urllib.error import URLError, HTTPError
import http.client
from socket import timeout

class Network(object):
    def getImage(self,url):
        image=self.getURL(url)
        ##ADD FILE VERIFICATION
        print(image.headers.items())
        return image

    def getVideo(self,url):
        video=self.getURL(url)
        video.headers.items()
        return video




    def getURL(self,url):
        liveURL = ''
        try:
            liveURL = urllib.request.urlopen(url, timeout=10)
        except urllib.error.URLError as e:
            print('Url Error code: ')
            print(e.reason)
            return False
            # return false, e.code
        except urllib.error.HTTPError as e:
            print('Reason: ', e.reason)
            return False
            # return false, e.reason
        except http.client.HTTPException as e:
            print(e)
            return False
        except urllib.error.ContentTooShortError as e:
            print(e)
            return False
        except timeout:
            print('timeout occured..trying next')
            return False
        except Exception as e:
            print(e)
            return False
        if liveURL == '':
            return False
        else:
            return liveURL




#checksLogger.error('generic exception: ' + traceback.format_exc())

'''
from socket import timeout
try:
    response = urllib.request.urlopen(url, timeout=10).read().decode('utf-8')
except (HTTPError, URLError) as error:
    logging.error('Data of %s not retrieved because %s\nURL: %s', name, error, url)
except timeout:
    logging.error('socket timed out - URL %s', url)
else:
    logging.info('Access successful.')





import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': '',
          'location': '',
          'language': '' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read()

'''