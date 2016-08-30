import os
import errno



class Parser(object):
    def __init__(self):
        True

    def formatImageName(self, url):
        try:
            filename = url.rsplit('tumblr_', 1)[1]
        except IndexError as e:
            print(e)
            return False
        else:
            return filename

    def formatVideoName(self, url):
        try:
            filename = url.rsplit('tumblr_', 1)[1] + '.mp4'
        except IndexError as e:
            print(e)
            return False
        else:
            return filename

    def writeFile(self, filename, file):
        localImage = open(filename, 'wb')
        localImage.write(file.read())
        localImage.close()

    def mkdirs(self, newdir, mode=0o777):
        try: os.makedirs(newdir, mode)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise exc
            pass
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

    def getDirectoryName(self, url):
        url =url.replace(".tumblr.com","")
        url = url.replace("http://","")
        url = url.replace("https://", "")
        url = 'blogs/'+url
        return url
