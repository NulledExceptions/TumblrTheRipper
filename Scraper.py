#!/usr/bin/env python3

from Network import Network
from Parser import Parser
from xml.dom import minidom
from xml.parsers.expat import ExpatError
from SQLLITE import SQLLITE
import logging




class Scraper(object):
    def __init__(self, tagging=False):
        self.tagging = tagging
        self.ignore_file_types=False
        # self.checklist = ('<tag>me</tag>', '<tag>mine</tag>','<tag>self</tag>','<tag>myself</tag>',
        #                   '<tag>personal</tag>','<tag>her</tag>')
        self.checklist = ('<tag>me</tag>')
        self.ignore_format=['.gif','.png']

    def scrapePage(self, url):

        scraperNetwork=Network()

        tumblrPage=scraperNetwork.getURL(url)
        if not (tumblrPage):
            pass

        try:
            xmldoc = minidom.parse(tumblrPage)
            postlist = xmldoc.getElementsByTagName('post')
        except ExpatError:
            logging.debug('unxexpected xml format')
            pass
        except AttributeError:
            logging.debug('unxexpected ATTRIBUTE ERROR')
            pass
            # log
            # return flase
        else:
            if((postlist or xmldoc)==False):
                pass
            for eachpost in postlist:
                #logging.debug(eachpost.attributes['type'].value)
                if (self.tagging):
                    if not self.checkTags(eachpost):
                        continue

                if eachpost.attributes['type'].value == 'photo':
                    caption = self.checkCaption(eachpost)
                    urls =eachpost.getElementsByTagName('photo-url')


                    for eachurl in urls:
                        imageUrl = self.getImageUrl(eachurl)
                        if imageUrl:
                            imageFile=scraperNetwork.getURL(imageUrl)
                            if imageFile:
                                #logging.debug(imageFile.headers.items())
                                imageFilename=Parser.formatImageName(imageUrl)
                                if(imageFilename):
                                    Parser.writeFile(imageFilename,imageFile)
                                    #logging.debug(eachpost.attributes.keys())
                                    image={
                                        'name':imageFilename,
                                        'caption':caption,
                                        'account':eachpost.attributes['id'].value,
                                        'url':eachpost.attributes['url'].value,
                                        'id': eachpost.attributes['id'].value,
                                        'source':eachpost.attributes['url-with-slug'].value

                                    }
                                    SQLLITE().insertImage(image)

                if eachpost.attributes['type'].value == 'video':
                    videoUrl= self.getVideoUrl(eachpost)
                    if videoUrl:
                        videoFile=scraperNetwork.getURL(videoUrl)
                        if videoFile:
                            videoFilename = Parser.formatVideoName(videoUrl)
                            if videoFilename:
                                Parser.writeFile(videoFilename,videoFile)

    def getTotalPosts(self,url):
        xmldoc = Network().getURL(url)
        if xmldoc:
            try:
                xmldoc = minidom.parse(xmldoc)
            except ExpatError:
                logging.debug('unxexpected xml format')
                return False
                #log
                #return flase
            except OSError:
                logging.debug('unxexpected os error ')
                return False


            else:

                try:
                    itemlist= xmldoc.getElementsByTagName('posts')
                    return itemlist[0].attributes['total'].value
                except ExpatError:
                    logging.debug("No posts or total, check url..")
                    #log
                    #return flase
                return False

    def getImageUrl(self,url):
        size = 0
        size = url.attributes['max-width'].value
        if (size == '1280'):
            # print 'obtaining image .. ' + a.childNodes[0].data
            return url.childNodes[0].data

        if (size == '500'):
            return url.childNodes[0].data


    def getVideoUrl(self,videopost):
        vidpost = videopost.childNodes[2].toxml()

        try:
            vidpost = vidpost.rsplit('source src=&quot;', 1)[1]
            vidsrc = vidpost.split('&quot; ')[0]

            if (vidsrc[-4:] == '/480'):
                vidsrc = vidsrc[:-4]
            return vidsrc
        except IndexError as e:
            logging.debug('error')
            logging.debug(e)
            logging.debug(IndexError)
            logging.debug(vidpost)
            pass
            #return flase , e

    def checkTags(self,eachpost):
        tags = eachpost.getElementsByTagName('tag')
        tags_found=False
        for tag in tags:
            # logging.debug(tag.toxml())
            if tag.toxml() in self.checklist:
                tags_found=True

        if tags_found:
            logging.info("match found")
            return True
        else:
            return False

    def checkCaption(self,eachpost):
        caption = eachpost.getElementsByTagName('photo-caption')
        if(caption.length==0):
            return None
        else:
            return caption[0].childNodes[0].nodeValue

