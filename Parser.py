#!/usr/bin/env python3
import os
import errno
from os.path import expanduser
import logging

class Parser(object):

    @staticmethod
    def formatImageName(url):
        try:
            filename = url.rsplit('tumblr_', 1)[1]
        except IndexError as e:
            logging.debug(e)
            return False
        else:
            return filename

    @staticmethod
    def formatVideoName(url):
        try:
            filename = url.rsplit('tumblr_', 1)[1] + '.mp4'
        except IndexError as e:
            logging.debug(e)
            return False
        else:
            return filename

    @staticmethod
    def writeFile(filename, file):
        localImage = open(filename, 'wb')
        try:
            localImage.write(file.read())
        except:
            logging.debug('there was an error writing file')
            localImage.close()
            pass
        localImage.close()

    @staticmethod
    def mkdirs(newdir, mode=0o777):
        home = expanduser("~")+'/Tumblr/'
        newdir=home+newdir
        try: os.makedirs(newdir, mode)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise exc
            pass
        os.chdir(newdir)


    @staticmethod
    def formatInput(input):
        ##STRIP WHITE SPACE!!

        if input[-1] == '/':
            input =input[:-1]
        if not input.endswith('.tumblr.com'):
            print ('Enter a valid tumblr domain')
            quit()

        if not (input.startswith('http://') or input.startswith('https://')):
            print ('Enter a valid url')
            quit()
        return input + '/api/read'

    @staticmethod
    def getDirectoryName(url, tagging):
        #readable, re would be better
        url = url.replace(".tumblr.com","")
        url = url.replace("http://","")
        url = url.replace("https://", "")

        if tagging:
            url = '[tag]' + url
        url = 'blogs/' + url
        return url
