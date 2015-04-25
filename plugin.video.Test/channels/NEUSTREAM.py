# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcaddon,os,base64,sys,xbmc,urlresolver
import cozucu, araclar
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json

Addon = xbmcaddon.Addon('plugin.video.Test')
__settings__ = xbmcaddon.Addon(id='plugin.video.Test')
__language__ = __settings__.getLocalizedString
IMAGES_PATH = xbmc.translatePath(os.path.join(Addon.getAddonInfo('path'), 'resources', 'images'))
addon_icon    = __settings__.getAddonInfo('icon')

fileName = "NEUSTREAM"

xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

def main():
        neustream="http://neu-stream.com/"
        araclar.addDir(fileName,'[COLOR red][B]>>>>>>>>>>>>>>>>>[/B][/COLOR][COLOR yellow][B] Film ARA - SEARCH[/B][/COLOR][COLOR red][B] <<<<<<<<<<<<<<<<<[/B][/COLOR]', "neustreamSearch()", "","special://home/addons/plugin.video.dream-clup/resources/images/ARAMA_SEARCH.png")
        araclar.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yeni Eklenen Filmler [/B][/COLOR]', "neustreamRecent(url)",neustream,"special://home/addons/plugin.video.dream-clup/resources/images/yeni.png")

                ##### KATEGORILERI OKU EKLE #####
        link=araclar.get_url(neustream)
        soup = BeautifulSoup(link)
        panel = soup.findAll("ul", {"class": "uMenuRoot"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('td'):
            a=li.find('a')
            url= a['href']
            name= li.text
            name=name.encode('utf-8', 'ignore')
            araclar.addDir(fileName,'[COLOR green][B][COLOR red]>[/COLOR]'+name+'[/B][/COLOR]', "neustreamRecent(url)",url,"")

def neustreamRecent(Url):
        neustreamgit=Url
        link=araclar.get_url(Url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"id": "allEntries"},smartQuotesTo=None)
        panel = panel[0].findAll("td", {"class": "entTd"})
        for i in range (len (panel)):
            url=panel[i].find('a')['href']
            name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
            thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
            araclar.addDir(fileName,'[COLOR cyan][B]'+name+'[/B][/COLOR]', "neustreamvideolinks(url,name)",url,thumbnail)
				
        #############    SONRAKI SAYFA  >>>> #############
        page=re.compile('<b class="swchItemA1"><span>.*?</span></b>  <a class="swchItem1" href="(.*?)" onclick=".*?"><span>(.*?)</span></a>').findall(link)
        for Url,name in page:
                araclar.addDir(fileName,'[COLOR blue][B]Sonraki Sayfa >>[/B][/COLOR]'+'[COLOR red][B]'+name+'[/B][/COLOR]', "neustreamRecent(url)",Url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")

        #############     ONCEKI SAYFA  <<<< #############
        page2=re.compile('<a class="swchItem1" href="(.*?)" onclick=".*?"><span>.*?</span></a> <b class="swchItemA1"><span>.*?</span></b>').findall(link)
        for Url in page2:
                araclar.addDir(fileName,'[COLOR red][B]Onceki Sayfa[/B][/COLOR]', "neustreamRecent(url)",Url,"special://home/addons/plugin.video.Test/resources/images/oncekisayfa.png")

        #############      ^^^^ANASAYFA^^^^      #############
        araclar.addDir(fileName,'[COLOR red][B]ANA SAYFA[/B][/COLOR]', "main()",Url,"special://home/addons/plugin.video.Test/resources/images/anasayfa.png")	

########	?	ARAMA	?	########
def neustreamSearch():
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            query=query.replace(' ','+')
            query=araclar.name_fix(query)
			
        try:
            araclar.addDir(fileName,'[COLOR blue][B]-----NEUSTREAM-----[/B][/COLOR]', "","","Search")
            Url = ('http://neu-stream.com/'+'?s='+query)
            link=araclar.get_url(Url)
            soup = BeautifulSoup(link)
            panel = soup.findAll("div", {"id": "allEntries"},smartQuotesTo=None)
            panel = panel[0].findAll("td", {"class": "entTd"})
            for i in range (len (panel)):
                url=panel[i].find('a')['href']
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                araclar.addDir(fileName,'[COLOR green][B]>> - [/B][/COLOR]'+name, "neustreamvideolinks(url,name)",url,thumbnail)

            #############    SONRAKI SAYFA  >>>> #############
            page=re.compile('<b class="swchItemA1"><span>.*?</span></b>  <a class="swchItem1" href="(.*?)" onclick=".*?"><span>(.*?)</span></a>').findall(link)
            for Url,name in page:
                    araclar.addDir(fileName,'[COLOR blue][B]Sonraki Sayfa >>[/B][/COLOR]'+'[COLOR red][B]'+name+'[/B][/COLOR]', "neustreamRecent(url)",Url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")

            #############     ONCEKI SAYFA  <<<< #############
            page2=re.compile('<a class="swchItem1" href="(.*?)" onclick=".*?"><span>.*?</span></a> <b class="swchItemA1"><span>.*?</span></b>').findall(link)
            for Url in page2:
                    araclar.addDir(fileName,'[COLOR red][B]Onceki Sayfa[/B][/COLOR]', "neustreamRecent(url)",Url,"special://home/addons/plugin.video.Test/resources/images/oncekisayfa.png")
        except:
            xbmc.executebuiltin('Notification("[COLOR yellow][B]SKY Center[/B][/COLOR]","[COLOR yellow][B]neustream Acilamadi[/B][/COLOR]")')

        araclar.addDir(fileName,'[COLOR yellow][B]YENI ARAMA YAP[/B][/COLOR]', "neustreamSearch()","","Search")
        araclar.addDir(fileName,'[COLOR red][B]ANA SAYFAYA GIT[/B][/COLOR]', "main()",Url,"anasayfa")
########   linkleri topla   ########
def neustreamvideolinks(url,name):
	link=araclar.get_url(url)
	match=re.compile('<a href="(.*?)" target="_blank"><img alt="(.*?)"').findall(link)
	for url,name in match:
                #print url
		araclar.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]'+name+'[/B][/COLOR]',"UrlResolver_Player(name,url)",url,"")
						
'''#############################################################################################'''
'''#############################################################################################'''
#######################################    VIDEO    ###############################################
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
