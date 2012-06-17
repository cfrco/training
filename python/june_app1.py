#!/usr/bin/env python 

import urllib2

def getTrueURL(url):
    res = urllib2.urlopen(url)
    for line in res :
        if "Lbjs.TargetUrl" in line :
            return line[line.find("'")+1:line.rfind("'")]

        
def getImgURLs(url):
    res = urllib2.urlopen(url)
    urls = []
    path = ""

    for line in res :
        if "<base" in line : #get basepath
            path = line[line.find("\"")+1:line.rfind("\"")]

        if "<td><img" in line: # focus on comic img
            img = line[line.find("\"")+1:line.rfind("\"")]
            urls += [path+img]

    return urls

def download_img(url):
    res = urllib2.urlopen(url)
    fp = open("./"+url[url.rfind("/")+1:]+".png","w") # +".png" fix filename
    for line in res :
        fp.write(line)
    fp.close()


#u =  getImgURLs( getTrueURL("http://a324fe5b.linkbucks.com/"))
#download_img(u[0])

furl = raw_input("please enter urlcode (http://________.linkbucks.com/ >> ")
urls = getImgURLs(getTrueURL("http://"+furl+".linkbucks.com/"))

for url in urls:
    print "downloading "+url +" ... "
    download_img(url)
