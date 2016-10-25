#!/usr/bin/env python3
import urllib.error
import urllib.request
from urllib.error import URLError, HTTPError
import http.client
from socket import timeout
import logging

class Network(object):
    @staticmethod
    def getUrlFileHeaders(url):
        file=Network.getURL(url)
        if file.header.items():
            return file.headers.items()
        else:
            return None
    @staticmethod
    def getFileHeaders(file):
        if file.headers.items():
            return file.headers.items()
        else:
            return None

    @staticmethod
    def getURL(url):
        liveURL = ''
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        try:
            liveURL = urllib.request.urlopen(req, timeout=10)
        except (urllib.error.HTTPError,urllib.error.URLError) as e:
            logging.error('Url Error code: ')
            logging.error(e.reason)
            return False

        except http.client.HTTPException as e:
            logging.error(e)
            return False
        except urllib.error.ContentTooShortError as e:
            logging.error(e)
            return False
        except http.client.IncompleteRead as icread:
            logging.error(icread.partial.decode('utf-8'))
            return False
        except timeout:
            logging.error('timeout occured..trying next')
            return False
        except Exception as e:
            logging.error(e)
            return False
        if liveURL == '':
            return False
        else:
            return liveURL




#checksLogger.error('generic exception: ' + traceback.format_exc())

'''

except (HTTPError, URLError) as error:
    logging.error('Data of %s not retrieved because %s\nURL: %s', name, error, url)
except timeout:
    logging.error('socket timed out - URL %s', url)
else:
    logging.info('Access successful.')

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