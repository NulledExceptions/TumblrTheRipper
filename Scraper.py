from Network import getURL
from xml.dom import minidom
import errno
from xml.parsers.expat import ExpatError


def scrapePage( url):
    tumblrPage=getURL(url)

    try:
        xmldoc = minidom.parse(tumblrPage)
        postlist = xmldoc.getElementsByTagName('post')
    except ExpatError:
        print 'unxexpected xml format'
        # log
        # return flase
    for eachpost in postlist:
        #print eachpost.attributes['type'].value
        if eachpost.attributes['type'].value == 'photo':
            urls =eachpost.getElementsByTagName('photo-url')
            for eachurl in urls:
                imageUrl = getImageUrl(eachurl)
                if imageUrl:
                    imageFile=getURL(imageUrl)
                    if imageFile:
                        imageFilename=formatImageName(imageUrl)
                        print imageFilename
                        writeFile(imageFilename,imageFile)

        if eachpost.attributes['type'].value == 'video':
            videoUrl= getVideoUrl(eachpost)
            if videoUrl:
                videoFile =getURL(videoUrl)
                if videoFile:
                    videoFilename = formatVideoName(videoUrl)
                    print videoFilename
                    writeFile(videoFilename,videoFile)

def getTotalPosts(url):
    xmldoc = getURL(url)
    if xmldoc:
        try:
            xmldoc = minidom.parse(xmldoc)
        except ExpatError:
            print 'unxexpected xml format'
            #log
            #return flase

        try:
            itemlist = xmldoc.getElementsByTagName('posts')
            return itemlist[0].attributes['total'].value
        except ExpatError:
            print "No posts or total, check url.."
            #log
            #return flase

def getImageUrl(url):
    size = 0
    size = url.attributes['max-width'].value
    if (size == '1280'):
        # print 'obtaining image .. ' + a.childNodes[0].data
        return url.childNodes[0].data

    if (size == '500'):
        return url.childNodes[0].data


def getVideoUrl(videopost):
    vidpost = videopost.childNodes[2].toxml()

    try:
        vidpost = vidpost.rsplit('source src=&quot;', 1)[1]
        vidsrc = vidpost.split('&quot; ')[0]

        if (vidsrc[-4:] == '/480'):
            vidsrc = vidsrc[:-4]
        return vidsrc
    except errno as e:
        print vidpost
        print 'error +'
        print errno
        pass
        #return flase , errno
    except IndexError as e:
        print 'error'
        print e
        print IndexError
        print vidpost
        pass
        #return flase , e

def formatImageName(url):
    filename =url[-30:]
    return filename

def formatVideoName(url):
    filename = url[-24:] + '.mp4'
    return filename

def writeFile(filename, file):
    localImage= open(filename,'wb')
    localImage.write(file.read())
    localImage.close()

