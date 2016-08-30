from Network import Network
from Parser import Parser
from xml.dom import minidom
from xml.parsers.expat import ExpatError
from DBSQLLite import DBSQLLite




class Scraper(object):
    def __init__(self):
        self.tagging = False
        self.checklist = []




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
                #print eachpost.attributes['type'].value
                if eachpost.attributes['type'].value == 'photo':
                    urls =eachpost.getElementsByTagName('photo-url')

                    if(self.tagging):
                        tags = eachpost.getElementsByTagName('tag')
                        if not (self.checkTags(self.checklist, tags)):
                            pass

                    for eachurl in urls:
                        imageUrl = self.getImageUrl(eachurl)
                        if imageUrl:
                            imageFile=scraperNetwork.getURL(imageUrl)
                            if imageFile:
                                imageFilename=scraperIO.formatImageName(imageUrl)
                                if(imageFilename):
                                    print (imageFilename)
                                    scraperIO.writeFile(imageFilename,imageFile)

                if eachpost.attributes['type'].value == 'video':
                    videoUrl= self.getVideoUrl(eachpost)
                    if videoUrl:
                        videoFile=scraperNetwork.getURL(videoUrl)
                        if videoFile:
                            videoFilename = scraperIO.formatVideoName(videoUrl)
                            if(videoFilename):
                                print (videoFilename)
                                scraperIO.writeFile(videoFilename,videoFile)

    def getTotalPosts(self,url):
        scraperNetwork=Network()

        xmldoc = scraperNetwork.getURL(url)
        if xmldoc:
            try:
                xmldoc = minidom.parse(xmldoc)
            except ExpatError:
                print('unxexpected xml format')
                #log
                #return flase

            try:
                itemlist = xmldoc.getElementsByTagName('posts')
                return itemlist[0].attributes['total'].value
            except ExpatError:
                print("No posts or total, check url..")
                #log
                #return flase

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


    def checkTags(self,checklist,tags):
        if(checklist==None):
            print('no checklist for tags available')
            return False
        if(tags==None):
            return False

        for word in checklist:
            if(word in tags):
                print('Tag Found')
                return True
        return False

