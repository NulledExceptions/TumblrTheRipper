#!/usr/bin/env python3

from Network import Network
from Parser import Parser
from xml.dom import minidom
from xml.parsers.expat import ExpatError
from DBSQLLite import DBSQLLite




class Scraper(object):
    def __init__(self):
        self.tagging = False
        self.checklist = ('<tag>me</tag>', '<tag>me</tag>')
        self.ignore_format=['.gif','.png']




    def scrapePage(self, url):
        scraperIO = Parser()
        scraperNetwork=Network()

        tumblrPage=scraperNetwork.getURL(url)
        if not (tumblrPage):
            pass

        try:
            xmldoc = minidom.parse(tumblrPage)
            postlist = xmldoc.getElementsByTagName('post')
        except ExpatError:
            print ('unxexpected xml format')
            pass
            # log
            # return flase
        else:
            if((postlist or xmldoc)==False):
                pass
            for eachpost in postlist:
                #print(eachpost.attributes['type'].value)
                if (self.tagging):
                    if not self.checkTags(eachpost):
                        continue

                if eachpost.attributes['type'].value == 'photo':
                    urls =eachpost.getElementsByTagName('photo-url')


                    for eachurl in urls:
                        imageUrl = self.getImageUrl(eachurl)
                        if imageUrl:
                            imageFile=scraperNetwork.getURL(imageUrl)
                            if imageFile:
                                #print(imageFile.headers.items())
                                imageFilename=scraperIO.formatImageName(imageUrl)
                                if(imageFilename):
                                    scraperIO.writeFile(imageFilename,imageFile)

                if eachpost.attributes['type'].value == 'video':
                    videoUrl= self.getVideoUrl(eachpost)
                    if videoUrl:
                        videoFile=scraperNetwork.getURL(videoUrl)
                        if videoFile:
                            videoFilename = scraperIO.formatVideoName(videoUrl)
                            if videoFilename:
                                scraperIO.writeFile(videoFilename,videoFile)

    def getTotalPosts(self,url):
        xmldoc = Network().getURL(url)
        if xmldoc:
            try:
                xmldoc = minidom.parse(xmldoc)
            except ExpatError:
                print('unxexpected xml format')
                return False
                #log
                #return flase
            except OSError:
                print('unxexpected os error ')
                return False


            else:

                try:
                    itemlist= xmldoc.getElementsByTagName('posts')
                    return itemlist[0].attributes['total'].value
                except ExpatError:
                    print("No posts or total, check url..")
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
            print('error')
            print(e)
            print(IndexError)
            print(vidpost)
            pass
            #return flase , e

    def checkTags(self,eachpost):
        tags = eachpost.getElementsByTagName('tag')
        tags_found=False
        for tag in tags:
            # print(tag.toxml())
            if tag.toxml() in self.checklist:
                tags_found=True

        if tags_found:
            print("match found")
            return True
        else:
            return False


