import urllib.request
from urllib.error import URLError, HTTPError
import http.client


class Network(object):
    def getImage(self,url):
        image=self.getURL(url)
        ##ADD FILE VERIFICATION

        image.headers.items()
        return image

    def getVideo(self,url):
        video=self.getURL(url)
        video.headers.items()
        return video




    def getURL(self,url):
        liveURL = ''
        try:
            liveURL = urllib.request.urlopen(url)
        except urllib.error.URLError as e:
            print('Url Error code: ', e.code)
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
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
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