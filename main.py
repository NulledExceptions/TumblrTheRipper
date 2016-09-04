#!/usr/bin/env python3
from Scraper import Scraper
from Parser import Parser
import os
from DBSQLLite import DBSQLLite
import atexit
import logging




def printPercentage(start, total):
    percent = float(start) / float(total) * 100
    print ("{0:.2f}".format(percent)+ "%  " + str(start) + " of total: " + str(total))


def cleanUp(url, current,total):
    logger = logging.getLogger(__name__)
    records = (url, current, total)
    logger.debug('Records: %s', records)
    logger.info('Updating records ...')
    #u
    #sql queries
def main():

    testurl= ''
    '''
    '''
    # baseInput = sys.argv[1]
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('Start blog: '+testurl)

    inputurl=Parser().formatInput(testurl)
    print (inputurl)
    dirname = Parser().getDirectoryName(testurl)
    print (dirname)
    Parser().mkdirs(dirname)
    os.chdir(dirname)

    total = Scraper().getTotalPosts(inputurl)
    records = (inputurl, '0', total)
    logger.debug('Records: %s', records)
    logger.info('Updating records ...')

    if(total and int(total)>0):
        start=0
        while( start <= int(total)):
             printPercentage(start, total)
             if(start ==0):
                 url=inputurl
             else:
                url= inputurl + '?start=' + str(start)
             Scraper().scrapePage(url)
             start += 20

        records=(inputurl,start,total)
        logger.debug('Records: %s', records)
        logger.info('Updating records ...')
        atexit.register(cleanUp, inputurl, start, total)

        # update records here

        logger.info('Finish updating records')

if __name__== '__main__':
    main()