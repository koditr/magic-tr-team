# -*- coding: utf-8 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import os,base64,time
import mechanize
import sys
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json
import cozuculer
from cozuculer import t


fileName ="Sinema2"

__settings__ = xbmcaddon.Addon(id='plugin.video.magicTR')

__language__ = __settings__.getLocalizedString

home = __settings__.getAddonInfo('path')

folders = xbmc.translatePath(os.path.join(home, 'resources', 'lib'))

sys.path.append(folders)
#-------------------------------------------------#
import xbmctools,fix
import cozuculer

#-------------------------------------------------#
xbmcPlayer = xbmc.Player()

playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
playList.clear()
#-------------------------------------------------#

addon_icon    = __settings__.getAddonInfo('icon')


def main():
        try:
                html = xbmctools.sifre4()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!-- Site-(.*?)-->').findall(html)
                for url in match:
                        xbmctools.addDir(fileName,'[COLOR red][B]>>>>>>>>>>>>>>>>>[/B][/COLOR][COLOR yellow][B] Film ARA - SEARCH[/B][/COLOR][COLOR red][B] <<<<<<<<<<<<<<<<<[/B][/COLOR]', "Search()", "","http://fs2.directupload.net/images/150212/sqoaaulb.jpg","http://fs1.directupload.net/images/150213/htof3hyc.jpg")
                        xbmctools.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR yellow][B]Yeni Eklenen Filmler [/B][/COLOR]', "Yeni(url)",url,"http://fs1.directupload.net/images/150212/w6az9wna.jpg","http://fs1.directupload.net/images/150213/htof3hyc.jpg")
                        if name in html:
                                match = re.compile('<!--SK-(.*?)-->').findall(html)
                                if match:
                                        for web in match:
                                                web=xbmctools.angel(base64.b64decode(str(web)))
                                                tr=re.compile('<isim>(.*?)</isim><link>(.*?)</link><resim>(.*?)</resim><thumb>(.*?)</thumb>').findall(web)
                                                for name,url,thumbnail,thumb in tr:
                                                        name=fix.decode_fix(name)
                                                        xbmctools.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]'+name+'[/B][/COLOR]', "Yeni(url)",url,thumbnail,thumb)                                                            
        except:
                showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                sys.exit()
#-----------------------------------------#

def Yeni(url):
        link=xbmctools.get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "three-column"})
        liste=BeautifulSoup(str(panel))
        for li in liste.findAll('figure'):
                a=li.find('a')
                img=li.find('img')
                url= a['href']
                name=a['title'].encode('utf-8', 'ignore')
                name=fix.decode_fix(name)
                thumbnail=img['src'].encode('utf-8', 'ignore')
                xbmctools.addDir(fileName,'[COLOR beige][B]'+name+'[/B][/COLOR]', "ayrisdirma(url)",url,thumbnail,thumbnail)
				
        page=re.compile('page-numbers current\'>.*?</span>\n<a class=\'page-numbers\' href=\'(.*?)\'>(.*?)</a>').findall(link)
        for url,name in page:
                xbmctools.addDir(fileName,'[COLOR blue][B]SAYFA >>[/B][/COLOR]'+'[COLOR red][B]'+name+'[/B][/COLOR]', "Yeni(url)",url,"special://home/addons/plugin.video.magicTR/resources/images/sonrakisayfa.png")



def Search():
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            url = (t+query)
            url=url.replace(' ',"+")
            Yeni(url)


def ayrisdirma(url):
        url=url+'/9'

        
        listeler=[]
        urller=[]
        link=xbmctools.get_url(url)
        soup = BeautifulSoup(link)
        panel=soup.find("div", {"id": "woca-pagination"})
        for a in panel.findAll('a'):
            url=a['href']
            name= a.text
            name=name
            if "-" in name:
                    
                    pass
            else:
                    
                        
                    listeler.append('[COLOR beige][B][COLOR red]>>[/COLOR]'+name+'[/B][/COLOR]')
                    urller.append(url)
                
        dialog = xbmcgui.Dialog()
        secenek = dialog.select('Izleme Secenekleri...',listeler)
        for i in range(len(listeler)):
         
         if secenek == i:

           url=urller[i]
           VIDEOLINKS(name,url)

           
           return url
         else:
           pass
def VIDEOLINKS(name,url):
        #---------------------------#
        urlList=[]
        #---------------------------#
        playList.clear()
        link=xbmctools.get_url(url)
        link=link.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
		#---------------------------------------------#
        ok=re.compile('src="http://ok.ru/videoembed/(.*?)"').findall(link)
        for url in ok:
                url = 'http://ok.ru/videoembed/'+str(url).encode('utf-8', 'ignore')
                cozuculer.ok_ru(url)

		#---------------------------------------------#
        vk_2=re.compile('src="http://vk.com/(.*?)"').findall(link)
        for url in vk_2:
                url = 'http://vk.com/'+str(url).encode('utf-8', 'ignore')
                cozuculer.vk_player(name,url)

		#---------------------------------------------#
        vk_3=re.compile('rc="http://snnyk.com/(.*?)"').findall(link)
        for url1 in vk_3:
                url1=url1.replace('&amp;', '&').replace('&#038;', '&').replace('%3A',':').replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%2F','/')
                url1 = 'http://snnyk.com/'+str(url1).encode('utf-8', 'ignore')
                link=xbmctools.get_url(url1)
                vkvk=re.compile('param\[5\] \+ \'(.*?)\' \+ param\[6\] \+ \'(.*?)\' \+ param\[7\] \+ \'(.*?)\' \+').findall(link)
                for oid,vidid,has in vkvk:
                        url='https://api.vk.com/method/video.getEmbed?oid='+oid+'&video_id='+vidid+'&embed_hash='+has
                        cozuculer.vk2_player(name,url)

		#---------------------------------------------#

        youtube=re.compile('youtube.com\/embed\/(.*?)"').findall(link)
        for url in youtube:
                url = 'http://www.youtube.com/embed/'+str(url).encode('utf-8', 'ignore')
                cozuculer.magix_player(name,url)

		#---------------------------------------------#
        mailru2=re.compile('<iframe src=.*?ttp://videoapi.my.mail.ru/videos/embed/mail/(.*?).html').findall(link)
        for mailrugelen in mailru2:
                url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+mailrugelen+'.html'
                value=[]
                value.append((name,cozuculer.MailRu_Player(url)))

        mailru3=re.compile('http://api.video.mail.ru/videos/embed/mail/(.*?).html').findall(link)
        for mailrugelen in mailru3:
                url = 'http://videoapi.my.mail.ru/videos/embed/mail/'+mailrugelen+'.html'
                value=[]
                value.append((name,cozuculer.MailRu_Player(url)))
		#---------------------------------------------#

        if not urlList:
                match=re.compile('flashvars="file=(.*?)%3F.*?" />').findall(link)
                if match:
                        for url in match:
                                VIDEOLINKS(name,url)
       
        if urlList:
                Sonuc=playerdenetle(name, urlList)
                for name,url in Sonuc:
                        xbmctools.addLink(name,url,'')
                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                        listitem.setInfo('video', {'name': name } )
                        playList.add(url,listitem=listitem)
                xbmcPlayer.play(playList)
     
def playerdenetle(name, urlList):
        value=[]
        import cozuculer
        for url in urlList if not isinstance(urlList, basestring) else [urlList]:
                if "mail.ru" in url:
                        value.append((name,cozuculer.MailRu_Player(url))) 
        if  value:
            return value
def name_fix(x):        
        x=x.replace('-',' ')
        return x[0].capitalize() + x[1:]

def replace_fix(x):        
        x=x.replace('&#8211;', '-').replace('&#038;', '&').replace('&amp;', '&')
        return x

def showMessage(heading='MagicTR', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )










