#!/usr/bin/env python3
from Scraper import Scraper
from Parser import Parser
from SQLLITE import SQLLITE
import atexit
import logging


def printPercentage(start, total):
    percent = float(start) / float(total) * 100
    print("{0:.2f}".format(percent)+ "%  " + str(start) + " of " + str(total))


def blogExists():
    carry_on= input('already exists. Would you like to continue anyways?(y/n)')
    if (carry_on =='y'):
        return True
    elif (carry_on =='n'):
        quit()
    else:
        blogExists()

def cleanUp(records):
    logger = logging.getLogger(__name__)
    logging.debug(records)
    logger.debug('Records: %s', records)
    logger.info('Updating records ...')
    #SQLLITE().insert(records)

def main():
    tagging = False
    testurl= 'http://abc.tumblr.com/'

    # baseInput = sys.argv[1]
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('Start blog: '+testurl)

    inputurl=Parser().formatInput(testurl)
    logging.info(inputurl)
    dirname = Parser().getDirectoryName(testurl,tagging)


    logging.info(dirname)
    Parser().mkdirs(dirname)
    records = {}
    records['total'] = Scraper().getTotalPosts(inputurl)
    records['account'] = inputurl
    records['current'] = 0
    logger.info('Records: %s', records)
    dbconn = SQLLITE()
    if(dbconn.query_account(records['account'])):
        blogExists()
    #if not (SQLLITE().insert_initials(records)):
    dbconn.insert(records)


    if(records['total'] and int(records['total'])>0):
        start=0
        while( start <= int(records['total'])):
             printPercentage(start, records['total'])
             if(start ==0):
                 url=inputurl
             else:
                url= inputurl + '?start=' + str(start)
             Scraper(tagging).scrapePage(url)
             start += 20
             records['current'] = 0

        records['current']=start-20
        #SQLLITE().insert(records)
        logger.debug('Records: %s', records)
        logger.info('Updating records ...')
        atexit.register(cleanUp, records)

        # update records here

        logger.info('Finish updating records')

if __name__== '__main__':
    main()