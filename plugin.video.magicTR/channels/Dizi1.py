# -*- coding: utf-8 -*-
import urllib,urllib2,xbmcplugin,xbmcgui,xbmcaddon,xbmc
import re
import os,base64,time
import mechanize
import sys
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP as BS
import simplejson as json

USER_AGENT 	= 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
ACCEPT 		= 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

fileName ="Dizi1"

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
                html = xbmctools.sifre()
                name=__settings__.getSetting("Name")
                login=__settings__.getSetting("Username")
                password=__settings__.getSetting("password")
                match = re.compile('<!-- D1(.*?)-->').findall(html)
                for web in match:
                        web=xbmctools.angel(base64.b64decode(web))
                        tr=re.compile('<link>(.*?)</link>').findall(web)
                        for url in tr:
                                xbmctools.addDir(fileName,'[COLOR red][B]>>>[/B][/COLOR] [COLOR orange][B]Arama/Search[/B][/COLOR]', "Arama()","","",'special://home/addons/plugin.video.magicTR/fanart.jpg' )
                                xbmctools.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR yellow][B]Enson Eklenen Diziler [/B][/COLOR]', "Yeni(url)",url,"special://home/addons/plugin.video.Test/resources/images/yeni.png",'special://home/addons/plugin.video.magicTR/fanart.jpg' )
                                xbmctools.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR lightblue][B]Yerli Diziler Hepsi[/B][/COLOR]', "Kategoriler()",url,"special://home/addons/plugin.video.Test/resources/images/yeni.png",'special://home/addons/plugin.video.magicTR/fanart.jpg' )
                                xbmctools.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR red][B]Yeni Yerli Diziler [/B][/COLOR]', "YeniDiziler()",url,"special://home/addons/plugin.video.Test/resources/images/yeni.png",'special://home/addons/plugin.video.magicTR/fanart.jpg' )
                                xbmctools.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR orange][B]Eski Yerli Diziler [/B][/COLOR]', "EskiDiziler()",url,"special://home/addons/plugin.video.Test/resources/images/yeni.png",'special://home/addons/plugin.video.magicTR/fanart.jpg' )
                                xbmctools.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR] [COLOR pink][B]Yarisma Programlari [/B][/COLOR]', "Yarisma()",url,"special://home/addons/plugin.video.Test/resources/images/yeni.png",'special://home/addons/plugin.video.magicTR/fanart.jpg' )
                      
        except:
                showMessage("[COLOR blue][B]MagicTR[/B][/COLOR]","[COLOR blue][B]IP Adresiniz Kitlendi[/B][/COLOR]","[COLOR red][B]Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]")
                dialog = xbmcgui.DialogProgress()
                dialog1 = xbmcgui.Dialog()
                dialog1.ok('[COLOR red][B]Hesabiniz Kitlendi[/B][/COLOR]','[COLOR yellow][B] Lutfen Musteri Hizmetlerine Basvurun!! koditr.media@gmail.com[/B][/COLOR]')
                sys.exit()
#-----------------------------------------#
def Kategoriler():
       
        html = xbmctools.sifre()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if name in html:
                match = re.compile('<!-- DK(.*?)-->').findall(html)
                if match:
                        for web in match:
                                web=xbmctools.angel(base64.b64decode(str(web)))
                                tr=re.compile('<link>(.*?)</link><isim>(.*?)</isim><resim>(.*?)</resim>').findall(web)
                                for url,name,thumbnail in tr:
                                        name=fix.decode_fix(name)
                                        xbmctools.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "Yeni(url)",url,thumbnail,thumbnail)


def EskiDiziler():
        html = xbmctools.sifre()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if name in html:
                match = re.compile('<!--EskiD(.*?)-->').findall(html)
                if match:
                        for web in match:
                                web=xbmctools.angel(base64.b64decode(str(web)))
                                tr=re.compile('<link>(.*?)</link><isim>(.*?)</isim><resim>(.*?)</resim>').findall(web)
                                for url,name,thumbnail in tr:
                                        name=fix.decode_fix(name)
                                        xbmctools.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "Yeni(url)",url,thumbnail,thumbnail)

def YeniDiziler():
        html = xbmctools.sifre()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if name in html:
                match = re.compile('<!--YeniDizi(.*?)-->').findall(html)
                if match:
                        for web in match:
                                web=xbmctools.angel(base64.b64decode(str(web)))
                                tr=re.compile('<link>(.*?)</link><isim>(.*?)</isim><resim>(.*?)</resim>').findall(web)
                                for url,name,thumbnail in tr:
                                        name=fix.decode_fix(name)
                                        xbmctools.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "Yeni(url)",url,thumbnail,thumbnail)


def Yarisma():
        html = xbmctools.sifre()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if name in html:
                match = re.compile('<!--Yarisma(.*?)-->').findall(html)
                if match:
                        for web in match:
                                web=xbmctools.angel(base64.b64decode(str(web)))
                                tr=re.compile('<link>(.*?)</link><isim>(.*?)</isim><resim>(.*?)</resim>').findall(web)
                                for url,name,thumbnail in tr:
                                        name=fix.decode_fix(name)
                                        xbmctools.addDir(fileName,'[COLOR beige][B][COLOR orange]>[/COLOR]'+name+'[/B][/COLOR]', "Yeni(url)",url,thumbnail,thumbnail)

def Arama():
        html = xbmctools.sifre()
        name=__settings__.getSetting("Name")
        login=__settings__.getSetting("Username")
        password=__settings__.getSetting("password")
        if name in html:
                match = re.compile('<!-- D1(.*?)-->').findall(html)
                if match:
                        for web in match:
                                        web=xbmctools.angel(base64.b64decode(web))
                                        tr=re.compile('<link>(.*?)</link>').findall(web)
                                        for dizi1 in tr:
                                                keyboard = xbmc.Keyboard("", 'Search', False)
                                                keyboard.doModal()
                                                if keyboard.isConfirmed():
                                                    query = keyboard.getText()
                                                    url = (dizi1+'/?s='+query)
                                                    Yeni(url)


def Yeni(url):
        link=xbmctools.get_url(url)
        soup = BeautifulSoup(link)
        panel = soup.findAll("div", {"class": "leftC"},smartQuotesTo=None)
        panel = panel[0].findAll("div", {"class": "moviefilm"})
        for i in range (len (panel)):
                url=panel[i].find('a')['href']
                name=panel[i].find('img')['alt'].encode('utf-8', 'ignore')
                thumbnail=panel[i].find('img')['src'].encode('utf-8', 'ignore')
                xbmctools.addDir(fileName,'[COLOR beige][B][COLOR blue]>[/COLOR]'+name+'[/B][/COLOR]',"dizivideolinks(url,name)",url,thumbnail,thumbnail)
         ####---------------Sonraki sayfa-------------------------------########
        page=re.compile('<span class=\'current\'>.*?</span><a class="page larger" href="(.*?)">(.*?)</a>').findall(link)
        for Url,name in page:
               
                xbmctools.addDir(fileName,'[COLOR blue][B]Sayfa >>[/B][/COLOR]'+'[COLOR red][B]'+name+'[/B][/COLOR]', "Yeni(url)",Url,"special://home/addons/plugin.video.magicTR/resources/images/sonrakisayfa.png")




def dizivideolinks(url,name):
        urlList=''
        ok=True
        link=xbmctools.get_url(url)
        match2=re.compile('href="(.*?)"><span>.*?</span>').findall(link)
        for partUrl in match2:
                urlList=urlList+partUrl 
                urlList=urlList+':;'
        total=url+':;'+urlList
        pDialog = xbmcgui.DialogProgress()
        ret = pDialog.create('Loading playlist...')
        match = total.split(':;')
        del match[-1]
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+':     '+'[B]' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+'[/B]'+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
        note='[COLOR pink]'+'http://www.xbmctr.tv'+'[/COLOR]'+'      '+'[COLOR beige][B]'+'magicTR Team'+'[/B][/COLOR]'
        pDialog.update(0,'[COLOR red][B]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/B][/COLOR]',remaining_display,note)
        i=0
        for url in match:
                i+=1
                name2=str(i)+'. Parça'
                
                link=xbmctools.get_url(url)
                try:
                        dm=re.compile('src="http://www.dailymotion.com/embed/video/(.*?)"').findall(link)
                        for url in dm:
                                url = 'http://www.dailymotion.com/embed/video/'+url
                                link=xbmctools.get_url(url)
                                if "stream_hls_url" in link:
                                        match=re.compile('"stream_hls_url":"(.*?)"').findall(link)
                                elif "stream_h264_ld_url" in link:                          
                                        match=re.compile('"stream_h264_ld_url":"(.*?)"').findall(link)
                                elif "stream_h264_url" in link:                            
                                        match=re.compile('"stream_h264_url":"(.*?)"').findall(link)
                                elif "stream_h264_hq_url" in link:         
                                        match=re.compile('"stream_h264_hq_url":"(.*?)"').findall(link)
                                elif "stream_h264_hd1080_url" in link: 
                                        match=re.compile('"stream_h264_hd1080_url":"(.*?)"').findall(link)
                                else:
                                        print "video yok"
                                for url in match:
                                        url=url.replace("\\","")
                                       
                                xbmctools.addLink(name+' '+'[COLOR beige][B]'+name2+'[/B][/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+':     '+'[B]' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+'[/B]'+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://www.xbmctr.tv'+'[/COLOR]'+'      '+'[COLOR beige][B]'+'magicTR Team'+'[/B][/COLOR]'
                                pDialog.update(percent,'[COLOR red][B]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/B][/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False

                except:
                        pass
               
                try:
                      vk=re.compile('vk.com\/(.*?)"').findall(link)
                      for url in vk:
                                url='http://vk.com/'+url

                                
                                url=url.replace('&#038;','&')
                                link=xbmctools.get_url(url)
                                match4=re.compile('"url480":"(.*?)"').findall(link)
                                for url in match4:
                                        url=url.replace('\/','/')
      
                                                
                                xbmctools.addLink(name+' '+'[COLOR beige][B]'+name2+'[/B][/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+':     '+'[B]' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+'[/B]'+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://www.xbmctr.tv'+'[/COLOR]'+'      '+'[COLOR beige][B]'+'magicTR Team'+'[/B][/COLOR]'
                                pDialog.update(percent,'[COLOR red][B]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/B][/COLOR]',remaining_display,note)
                                time.sleep(3)
                                pDialog.close()
                                if (pDialog.iscanceled()):
                                        return False

                                


                except:
                        pass

                
                try:
                        
                        yt=re.compile("encodeURIComponent\(\'(.*?)\'").findall(link)
                        for url in yt:
                                
                                url=url.replace('http://www.youtube.com/watch?v=','')
                                url='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(url)
                                xbmctools.addLink(name+' '+'[COLOR beige][B]'+name2+'[/B][/COLOR]',url,'')
                                listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                listitem.setInfo('video', {'name': name } )
                                playList.add(url,listitem=listitem)
                                loadedLinks = loadedLinks + 1
                                percent = (loadedLinks * 100)/totalLinks
                                remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+':     '+'[B]' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+'[/B]'+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                note='[COLOR pink]'+'http://www.xbmctr.tv'+'[/COLOR]'+'      '+'[COLOR beige][B]'+'magicTR Team'+'[/B][/COLOR]'
                                pDialog.update(percent,'[COLOR red][B]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/B][/COLOR]',remaining_display,note)
                                if (pDialog.iscanceled()):
                                        return False
                        
                                

                except:

                        pass

                
                try:
                        mr=re.compile('value="movieSrc=(.*?)&amp;mp4=1&').findall(link)#
                        for url in mr:
                                
                            url= 'http://videoapi.my.mail.ru/videos/embed/'+str(url)+'.html'
                            req = urllib2.Request(url)

                            resp = urllib2.urlopen(req)
                            html = resp.read()
                            cookie_string = resp.headers.getheader('Set-Cookie').split(';')[0]

                            print resp.headers.getheader('Set-Cookie')
                            headers = {
                                'Cookie': cookie_string
                            }

                            metadata_url_start = html.find('metadataUrl') + len('metadataUrl":"')
                            metadata_url_end = html.find('"', metadata_url_start)
                            metadata_url = html[metadata_url_start:metadata_url_end]

                            metadata_response =  urllib2.urlopen(metadata_url)
                            metadata = json.loads(metadata_response.read()) 

                            #---------------------------------#
                            xbmc_cookies = '|Cookie=' + urllib.quote(cookie_string)
                            streams = [(v['key'], v['url'] + xbmc_cookies) for v in metadata['videos']]
                            if streams >0:
                                    del streams[0]
                                  
                                    
                                    for name2,url2 in streams:
                                            
                                            
                                        xbmctools.addLink(name+' '+'[COLOR beige][B]'+name2+'[/B][/COLOR]',url2,'')
                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                        listitem.setInfo('video', {'name': name } )
                                        playList.add(url2,listitem=listitem)
                                        loadedLinks = loadedLinks + 1
                                        percent = (loadedLinks * 100)/totalLinks
                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+':     '+'[B]' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+'[/B]'+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                        note='[COLOR pink]'+'http://www.xbmctr.tv'+'[/COLOR]'+'      '+'[COLOR beige][B]'+'magicTR Team'+'[/B][/COLOR]'
                                        pDialog.update(percent,'[COLOR red][B]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/B][/COLOR]',remaining_display,note)
                                        if (pDialog.iscanceled()):
                                                return False
                                

                            else:
                                    pass

                except:
                        pass
                try:
                        ok=re.compile('http://ok.ru/videoembed/(.*?)"').findall(link)
                        for url in ok:
                                
                                url='http://ok.ru/videoembed/'+str(url)
                                sources = []

                                if(re.search(r'ok.ru', url)):
                                        print
                                        
                                        id = re.search('\d+', url).group(0)
                                        jsonUrl = 'http://ok.ru/dk?cmd=videoPlayerMetadata&mid=' + id
                                        jsonSource = json.loads(http_req(jsonUrl))

                                        for source in jsonSource['videos']:

                                                        name = '%s %s' % ('', source['name'])
                                                        link = '%s|User-Agent=%s&Accept=%s&Referer=%s' % (source['url'], USER_AGENT, ACCEPT, urllib.quote_plus(url))
                                                        url4 = link
                                                        if "mob" in name:
                                                                pass
                                                        else:
                                                                if "lowe" in name:
                                                                        pass
                                                                else:
                                                                        if "sd" in name:
                                                                                pass
                                                                        else:
                                                                                if "h" in name:
                                                                                        pass
                                                                                else:
                                                                                        xbmctools.addLink(name+' '+'[COLOR beige][B]'+name+'[/B][/COLOR]',url4,'')
                                                                                        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage='')
                                                                                        listitem.setInfo('video', {'name': name } )
                                                                                        playList.add(url4,listitem=listitem)
                                                                                        loadedLinks = loadedLinks + 1
                                                                                        percent = (loadedLinks * 100)/totalLinks
                                                                                        remaining_display ='[COLOR yellow]'+'Islem Yapilan Video Sayisi'+':     '+'[B]' +str(loadedLinks)+'[/COLOR]'+'[COLOR blue]'+' / '+'[/COLOR]'+'[COLOR green]'+str(totalLinks)+'[/B]'+'[/COLOR]'+'[COLOR lightgreen]'+'   '+'Video Bulundu'+'[/COLOR]'
                                                                                        note='[COLOR pink]'+'http://www.xbmctr.tv'+'[/COLOR]'+'      '+'[COLOR beige][B]'+'magicTR Team'+'[/B][/COLOR]'
                                                                                        pDialog.update(percent,'[COLOR red][B]'+'Videolar Olusturuluyor... Lutfen Bekleyin'+'[/B][/COLOR]',remaining_display,note)
                                                                                        if (pDialog.iscanceled()):
                                                                                                return False
                except:
                        pass

        xbmcPlayer.play(playList)
        
        
                                             

def showMessage(heading='IPTV', message = '', times = 5000, pics = addon_icon):
		try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
		except Exception, e:
			xbmc.log( '[%s]: showMessage: exec failed [%s]' % (addon_id, e), 2 )
def http_req(url, getCookie=False):
	req = urllib2.Request(url)
	req.add_header('User-Agent', USER_AGENT)
	req.add_header('Accept', ACCEPT)
	req.add_header('Cache-Control', 'no-transform')
	response = urllib2.urlopen(req)
	source = response.read()
	response.close()
	if getCookie:
		cookie = response.headers.get('Set-Cookie')
		return {'source': source, 'cookie': cookie}
	return source








