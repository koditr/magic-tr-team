# -*- coding: utf-8 -*-
##this script creates earch page for all related web sites in this addon
##created by drascom in date:18.03.2013
##it's not commercial free to use change all code


import xbmcplugin,xbmcgui,xbmcaddon,xbmc,urllib,urllib2,os,sys,re
import araclar,cozucu


Addon = xbmcaddon.Addon('plugin.video.Test')
__settings__ = xbmcaddon.Addon(id='plugin.video.Test')
__language__ = __settings__.getLocalizedString

from BeautifulSoup import BeautifulSoup 




def main():
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            query=query.replace(' ','+')
            query=araclar.name_fix(query)

  
       


        
        try:
                fileName ="FILMIZLE"
                araclar.addDir(fileName,'[COLOR blue][B] --- FILMIZLE SONUCLARI ---[/B][/COLOR]',"","","")
                url = ('http://www.indirmedenfilmizlee.net/index.php?s='+query)
                link=araclar.get_url(url)  
                match=re.compile('<a href="(.*?)" title="(.*?)">\n<img src="(.*?)" alt=".*?" /').findall(link)
                for url,name,thumbnail in match:
                        araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail)
        except:
                    xbmc.executebuiltin('Notification("Media Center","FILMIZLE Acilamadi")')

        try:
                fileName ="FILMIZLETIR"
                araclar.addDir(fileName,'[COLOR blue][B] --- FILMIZLETIR SONUCLARI ---[/B][/COLOR]',"","","")
                url = ('http://www.filmizletir.net/?s='+query)
                link=araclar.get_url(url)  
                match=re.compile('<a  href="(.*?)" title="(.*?)"><img src="(.*?)" width="129" height="191" alt=".*?" />').findall(link)
                for url,name,thumbnail in match:
                        araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail)
        except:
                    xbmc.executebuiltin('Notification("Media Center","FILMIZLETIR Acilmadi")')

        try:
                fileName ="FILMIZLEX"
                araclar.addDir(fileName,'[COLOR blue][B] --- FILMIZLEX SONUCLARI ---[/B][/COLOR]',"","","")
                url = ('http://www.filmizlexx.com/?s='+query+'&sa=search&scat=0)
                link=araclar.get_url(url)  
                match=re.compile('\n                    <a href="(.*?)" title="(.*?)" class="preview" rel="(.*?)"><img width="75" height="75" src=".*?" class="attachment-ad-thumb" alt=".*?" /></a>                \n').findall(link)
                for url,name,thumbnail in match:
                        araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail)
        except:
                    xbmc.executebuiltin('Notification("Media Center","FILMIZLEX Acilmadi")')

        try:
                fileName ="FILMSITE"
                araclar.addDir(fileName,'[COLOR blue][B] --- FILMSITE SONUCLARI ---[/B][/COLOR]',"","","")
                url = ('http://www.filmsiteleri.net/?s='+query)
                link=araclar.get_url(url)       
                match=re.compile('<a  href="(.*?)" title="(.*?)"><img src="(.*?)" width="129" height="191" alt=".*?" /></a>').findall(link)
                for url,name,thumbnail in match:
                       
                        araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail)
        except:
                    xbmc.executebuiltin('Notification("Media Center","FILMSITE Acilmadi")')

##        try:
##                fileName ="LOAD7"
##                araclar.addDir(fileName,'[COLOR blue][B] --- LOAD7 SONUCLARI ---[/B][/COLOR]',"","","")
##                url = ('http://www.film-izle.biz/index.php?s='+query)
##                link=araclar.get_url(url)  
##                match=re.compile('<a href="(.*?)"><img src="(.*?)"  alt="(.*?)" height="207" width="140"').findall(link)
##                for url,thumbnail,name in match:
##                        araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail)
##        except:
##                    xbmc.executebuiltin('Notification("Media Center","LOAD7 Acilmadi")')


