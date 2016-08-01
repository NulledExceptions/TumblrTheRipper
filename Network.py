import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError


def getImage(url):
    image=getURL(url)
    ##ADD FILE VERIFICATION

    image.headers.items()
    return image

def getVideo(url):
    video=getURL(url)
    video.headers.items()
    return video




def getURL(url):
    liveURL = ''
    try:
        liveURL = urllib2.urlopen(url)

    except HTTPError as e:
        print 'Error code: ', e.code
        return False
        # return false, e.code
    except URLError as e:
        print 'Reason: ', e.reason
        return False
        # return false, e.reason
    if liveURL =='':
        return False
    return liveURL




