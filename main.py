#!/usr/bin/env python3
from Scraper import Scraper
from Parser import Parser
import os
from DBSQLLite import DBSQLLite

def printPercentage(start, total):
    percent = float(start) / float(total) * 100
    print ("{0:.2f}".format(percent)+ "%  " + str(start) + " of total: " + str(total))

def main():

    testurl= 'http://abc.tumblr.com/'
    '''
    '''
    # baseInput = sys.argv[1]

    initialScraper = Scraper()

    inputurl=Parser().formatInput(testurl)
    print (inputurl)
    dirname = Parser().getDirectoryName(testurl)
    print (dirname)
    Parser().mkdirs(dirname)
    os.chdir(dirname)

    total = initialScraper.getTotalPosts(inputurl)
    if(total and int(total)>0):
        start=0
        while( start <= int(total)):
             printPercentage(start, total)
             if(start ==0):
                 url=inputurl
             else:
                url= inputurl + '?start=' + str(start)
             initialScraper.scrapePage(url)
             start += 20


if __name__== '__main__':
    main()