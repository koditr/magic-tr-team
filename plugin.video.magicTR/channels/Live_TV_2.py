# -*- coding: iso-8859-9 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import os,base64,time
import mechanize
import sys




fileName ="Live_TV_2"

__settings__ = xbmcaddon.Addon(id='plugin.video.magicTR')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
#-------------------------------------------------#
import xbmctools
import cozuculer

#-------------------------------------------------#
xbmcPlayer = xbmc.Player()

playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
#-------------------------------------------------#

addon_icon    = __settings__.getAddonInfo('icon')





def main():
        
#------------------------------------------------#
        try:
                html = xbmctools.sifre2()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
##                match3 = re.compile('<!--URL2-(.*?)-->').findall(html)
##                for url in match3:
##                        link=xbmctools.get_url(url)
##                        match1=re.compile('href="(.*?)"><span style=".*?">(.*?)</span>').findall(link)
##                        for url,name in match1:
##                                xbmctools.addDir(fileName,'[COLOR blue][B] >>[/B][/COLOR]'+ '[COLOR red][B]'+name+'[/B][/COLOR]', "tv(url)",url,"")
                match = re.compile('<!--#li2#(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools.angel(base64.b64decode(web))
                        tr=re.compile('<isim>(.*?)</isim>\n  <link>(.*?)</link>\n  <thumbnail>(.*?)</thumbnail>').findall(web)
                        for name,url,Thumbnail in tr:
                                url=url.replace('<![CDATA[','').replace(']]>','')
                                if "Beyaz" in name:
                                        pass
                                else:
                                        if "Fox" in name:
                                                pass
                                        else:
                                                xbmctools.addDir(fileName,name,"VideoLinks(name,url)",url,Thumbnail,Thumbnail)                     
        except:
                showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                sys.exit()
#-----------------------------------------#
def VideoLinks(name,url):
        xbmcPlayer = xbmc.Player()
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playList.clear()
        xbmctools.addLink('RETURN List << ','','')
        listitem = xbmcgui.ListItem(name)
        playList.add(url, listitem)
        xbmcPlayer.play(playList)
        exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
        if exec_version < 14.0:
                xbmctools.playlist()
        else:
                xbmctools.playlist2()
def VideoLinks2(name,url):
        link=xbmctools.get_url(url)
        match=re.compile('file: "(.*?)"').findall(link)
        for url in match:
                
                xbmcPlayer = xbmc.Player()
                playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                playList.clear()
                xbmctools.addLink('RETURN List << ','','')
                listitem = xbmcgui.ListItem(name)
                playList.add(url, listitem)
                xbmcPlayer.play(playList)
                exec_version = float(str(xbmc.getInfoLabel("System.BuildVersion"))[0:4])
                if exec_version < 14.0:
                        xbmctools.playlist()
                else:
                        xbmctools.playlist2()
def tv(url):
        link=xbmctools.get_url(url)
        match1=re.compile('href="(.*?)"><img width=".*?" height=".*?" src="(.*?)" class=".*?" alt="(.*?)" />').findall(link)
        for url,thumbnail,name in match1:
                xbmctools.addDir(fileName,'[COLOR beige][B][COLOR red]>>[/COLOR]'+name+'[/B][/COLOR]', "VideoLinks2(name,url)",url,thumbnail,thumbnail)



def showMessage(heading='IPTV', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )










