#!/usr/bin/env python3
import os
import errno
from os.path import expanduser
import logging




class Parser(object):
    #remove instantiation, make methods static
    def __init__(self):
        pass

    def formatImageName(self, url):
        try:
            filename = url.rsplit('tumblr_', 1)[1]
        except IndexError as e:
            logging.debug(e)
            return False
        else:
            return filename

    def formatVideoName(self, url):
        try:
            filename = url.rsplit('tumblr_', 1)[1] + '.mp4'
        except IndexError as e:
            logging.debug(e)
            return False
        else:
            return filename

    def writeFile(self, filename, file):
        localImage = open(filename, 'wb')
        try:
            localImage.write(file.read())
        except:
            logging.debug('there was an error writing file')
            localImage.close()
            pass
        localImage.close()

    def mkdirs(self, newdir, mode=0o777):
        home = expanduser("~")+'/Tumblr/'
        newdir=home+newdir
        try: os.makedirs(newdir, mode)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise exc
            pass
        os.chdir(newdir)
    ##STRIP WHITE SPACE
    def formatInput(self, input):
        if input[-1] == '/':
            input =input[:-1]
        if not input.endswith('.tumblr.com'):
            print ('Enter a valid tumblr domain')
            quit()

        if not (input.startswith('http://') or input.startswith('https://')):
            print ('Enter a valid url')
            quit()
        return input + '/api/read'

    def getDirectoryName(self, url, tagging):
        #readable, re would be better
        url = url.replace(".tumblr.com","")
        url = url.replace("http://","")
        url = url.replace("https://", "")

        if tagging:
            url = '[tag]' + url
        url = 'blogs/' + url
        return url
