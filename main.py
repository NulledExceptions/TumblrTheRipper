from Scraper import scrapePage, getTotalPosts

import time, os, errno


def mkdirs(newdir, mode=0777):
    try: os.makedirs(newdir, mode)
    except OSError, err:
        # Reraise the error unless it's about an already existing directory
        if err.errno != errno.EEXIST or not os.path.isdir(newdir):
            os.chdir(newdir)
            #raise
    os.chdir(newdir)


def formatInput(input):
    if input[-1] == '/':
        input =input[:-1]
    if not input.endswith('.tumblr.com'):
        print 'Enter a valid tumblr domain'
        quit()

    if not (input.startswith('http://') or input.startswith('https://')):
        print 'Enter a valid url'
        quit()
    return input + '/api/read'


def printPercentage(start, total):
    percent = float(start) / float(total) * 100
    print "{0:.2f}".format(percent)+ "%  " + str(start) + " of total: " + str(total)

def getDirectoryName(url):
    url =url.replace(".tumblr.com","")
    url = url.replace("http://","")
    url = url.replace("https://", "")
    return url



def main():

    testurl= ''
    # baseInput = sys.argv[1]

    inputurl=formatInput(testurl)
    print inputurl
    dirname = getDirectoryName(testurl)
    print dirname
    mkdirs(dirname)

    total = getTotalPosts(inputurl)
    if(total and total>0):
        start=0
        while( start <= int(total)):
             printPercentage(start, total)
             if(start ==0):
                 url=inputurl
             else:
                url= inputurl + '?start=' + str(start)
             scrapePage(url)
             start += 20


if __name__== '__main__':
    main()