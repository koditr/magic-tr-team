# -*- coding: utf-8 -*-
import xbmcplugin,xbmcgui,xbmcaddon,xbmc,urllib,urllib2,os,sys,re
import araclar,cozucu
import urllib,urllib2,re,cookielib

from BeautifulSoup import BeautifulSoup
import urlresolver

Addon = xbmcaddon.Addon('plugin.video.dream-clup')
__settings__ = xbmcaddon.Addon(id='plugin.video.dream-clup')
__language__ = __settings__.getLocalizedString
addon_icon    = __settings__.getAddonInfo('icon')

fileName ="KKISTE"
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)


############# ANA GIRIS KLASORLERI ##############################
def main():
        url='http://kkiste.to/genres/'
        #araclar.addDir(fileName,name,"mode(name,url)",url,thumbnail)
        araclar.addDir(fileName,'[COLOR red][B]>  -  [/B][/COLOR][COLOR yellow][B] SUCHE - SEARCH[/B][/COLOR][COLOR red][B]  -  <[/B][/COLOR]', "Search()", "","special://home/addons/plugin.video.dream-clup/resources/images/ARAMA_SEARCH.png")
        araclar.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]KINO Filme [/B][/COLOR]', "Yeni(name,url)",'http://kkiste.to/aktuelle-kinofilme/',"special://home/addons/plugin.video.dream-clup/resources/images/yeni.png" )
        araclar.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Neue Filme [/B][/COLOR]', "Yeni(name,url)",'http://kkiste.to/neue-filme/',"special://home/addons/plugin.video.dream-clup/resources/images/yeni.png" )
        link=araclar.get_url(url)  
        match=re.compile('<a href="(.*?)" title=".*?">(.*?)<span>').findall(link)
        for url,name in match:
                url = 'http://kkiste.to'+url
                print url
                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"Yeni(name,url)",url,'')

###################################################################                

                                                
######                       
def Search():
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            url = ('http://kkiste.to/search/?q='+query)
            Ara(url)
def Ara(url):
        link=araclar.get_url(url)  
        match=re.compile('<a href="(.*?)" title=".*?" class="title">(.*?)</a>\n<ul class="star-rating">').findall(link)
        for url,name in match:
                url = 'http://kkiste.to'+url
                print url
                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"tek(name,url)",url,'')

############
def Yeni(name,url):
        link=araclar.get_url(url)  
        match=re.compile('<a href="(.*?)" title=".*?" class="image">\n<img src="(.*?)" width="170" height="120" alt="(.*?)Stream"').findall(link)
        for url,thumbnail,name in match:
                url = 'http://kkiste.to'+url
                print url
                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"tek(name,url)",url,thumbnail)
                print thumbnail
        match1=re.compile('class="current_page">.*?</li><li><a href="(.*?)">(.*?)</a>').findall(link)
        for a,name in match1:
                name='Seite > - '+name
                url='http://kkiste.to/aktuelle-kinofilme/'+a
                print url
                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"Yeni(name,url)",url,'')
###########        
        
      
def tek(name,url):
        playList.clear()
        link=araclar.get_url(url)  
        match=re.compile('<a href="http://www.ecostream.tv/stream/(.*?).html" target="_blank">(.*?) <small>\[(.*?)\]</small>').findall(link)
        for url,name1,name2 in match:
                
                url='http://www.ecostream.tv/stream/'+url+'.html?ss=1'
                name=name1+' - - '+name2
                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"UrlResolver_Player(name,url)",url,'')


def UrlResolver_Player(name,url):
        UrlResolverPlayer = url
        playList.clear()
        media = urlresolver.HostedMediaFile(UrlResolverPlayer)
        source = media
        if source:
                url = source.resolve()
                araclar.addLink(name,url,'')
                araclar.playlist_yap(playList,name,url)
                xbmcPlayer.play(playList)
        else:
             showMessage('Acilamadi', 'iptal edildi')

def showMessage(heading='SKYMC', message = '', times = 3000, pics = addon_icon):
	try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading.encode('utf-8'), message.encode('utf-8'), times, pics.encode('utf-8')))
	except Exception, e:
		xbmc.log( '[%s]: showMessage: Transcoding UTF-8 failed [%s]' % (addon_id, e), 2 )
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 3 )
        
