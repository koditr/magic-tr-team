# -*- coding: utf-8 -*-

# for more info please visit http://xbmctr.com
'''
Created on 21 sempember 2012

@author: drascom
@version: 0.2.0

'''

import os
import sys
import urllib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import araclar
addon_id = 'plugin.video.Test'
__settings__ = xbmcaddon.Addon(id=addon_id)
home = __settings__.getAddonInfo('path')
fanart = xbmc.translatePath( os.path.join( home, 'fanart.png' ) )
# Fetch all folders needed to run the add on
folders = xbmc.translatePath(os.path.join(home, 'channels'))

sys.path.append(folders)
IMAGES_PATH = xbmc.translatePath(os.path.join(home, 'resources','images'))
sys.path.append(IMAGES_PATH)




def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param
    
    
params = get_params()
name = None
fileName = None
mode = None
url = None
thumbnail = None

#Try-catch blocks to see which parameters are available 
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    fileName = urllib.unquote_plus(params["fileName"])
except:
    pass
try:
    mode = urllib.unquote_plus(params["mode"])
except:
    pass
try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    thumbnail = urllib.unquote_plus(params["thumbnail"])
except:
    pass

print "Ad: "+str(name)
print "Dosya: "+str(fileName)
print "mode: "+str(mode)
print "Url: "+str(url)
print "Resim: "+str(thumbnail)


if fileName == None:
    fileName=''
    araclar.loadImports(folders)
    araclar.listChannels(IMAGES_PATH)
    
    #print 'kanallar:'+str(imps)
else:
    exec "import "+fileName+" as channel"
    exec "channel."+str(mode)

xbmcplugin.endOfDirectory(int(sys.argv[1]))



