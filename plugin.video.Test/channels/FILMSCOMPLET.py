# -*- coding: utf-8 -*-
import xbmcplugin,xbmcgui,xbmcaddon,xbmc,urllib,urllib2,os,sys,re
import araclar,cozucu


Addon = xbmcaddon.Addon('plugin.video.Test')
__settings__ = xbmcaddon.Addon(id='plugin.video.Test')
__language__ = __settings__.getLocalizedString


fileName ="FILMSCOMPLET"
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)


############# ANA GIRIS KLASORLERI ##############################
def main():
        url='http://filmscomplet.com/'
        #araclar.addDir(fileName,name,"mode(name,url)",url,thumbnail)
##        araclar.addDir(fileName,'[COLOR red][B]>>>>>>>>>>>>>>>>>[/B][/COLOR][COLOR yellow][B] Film ARA - SEARCH[/B][/COLOR][COLOR red][B] <<<<<<<<<<<<<<<<<[/B][/COLOR]', "Search()", "","special://home/addons/plugin.video.Test/resources/images/ARAMA_SEARCH.png")
        araclar.addDir(fileName,'[COLOR orange][B]>>[/B][/COLOR][COLOR beige][B] Accueil [/B][/COLOR]', "session(url)",url,"special://home/addons/plugin.video.Test/resources/images/yeni.png" )
##        #araclar.addDir(fileName,'[COLOR red][B]>>[/B][/COLOR][COLOR pink][B] Editorun Sectikleri [/B][/COLOR]', "Edit(url)",url,"")
##        araclar.addDir(fileName,'[COLOR gold][B]>>[/B][/COLOR][COLOR beige][B] Turkce Dublaj Filmler [/B][/COLOR]', "Dublaj(url)","http://www.baglanfilmizle.com/film-izle/izleme-secenekleri/turkce-dublaj","")
##        araclar.addDir(fileName,'[COLOR green][B]>>[/B][/COLOR][COLOR lightgreen][B] Yerli Filmler [/B][/COLOR]', "Yerli(url)","http://www.baglanfilmizle.com/film-izle/yerli-filmler)","")
##        ##### KATEGORILERI OKU EKLE ##########################
        
        link=araclar.get_url(url)
        match=re.compile('<li class="cat-item cat-item-.*?"><a href="(.*?)" title=".*?">(.*?)</a>').findall(link)
        for url,name in match:
                araclar.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR][COLOR beige][B]'+ name+'[/B][/COLOR]',"Yeni(url)",url,"")

###################################################################                

                                                
######                       
##def Search():
##        keyboard = xbmc.Keyboard("", 'Search', False)
##        keyboard.doModal()
##        if keyboard.isConfirmed():
##            query = keyboard.getText()
##            url = ('http://www.indirmedenfilmizlee.net/index.php?s='+query)
##            Yeni(url)

############
def Yeni(url):
        link=araclar.get_url(url)  
        match=re.compile('<a href=".*?"><img class=\'ep_thumb\' src=\'(.*?)\' alt=\'.*?\'  /></a>\r\n                \r\n\r\n                <div class="post_content">\r\n                    <h2 class="postitle"><a href="(.*?)">(.*?)</a>').findall(link)
        for thumbnail,url,name in match:
                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail)

        page=re.compile('<a href=\'(.*?)\' class=\'page larger\'>(.*?)</a>').findall(link)
        
        for url,name in page:
                araclar.addDir(fileName,'[COLOR purple][B]>>SAYFA-' + name+'[/B][/COLOR]',"Yeni(url)",url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")                     
        
###########        
def session(url):
        link=araclar.get_url(url)       
        match=re.compile('<a href="(.*?)"><img class=\'ep_thumb\' src=\'(.*?)\' alt=\'.*?\'  /></a>\r\n\r\n                \r\n                <div class="post_content">\r\n                    <h2 class="postitle"><a href=".*?">(.*?)</a>').findall(link)
        for url,thumbnail,name in match:
                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail)

        page=re.compile('<a href=\'(.*?)\' class=\'page larger\'>(.*?)</a>').findall(link)
        
        for url,name in page:
                araclar.addDir(fileName,'[COLOR purple][B]>>SAYFA-' + name+'[/B][/COLOR]',"session(url)",url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")                     
                                   
    

        
#############
def VIDEOLINKS(name,url):
        xbmcPlayer = xbmc.Player()
        playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playList.clear()

        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        link=link.replace('\xf6',"o").replace('\xd6',"O").replace('\xfc',"u").replace('\xdd',"I").replace('\xfd',"i").replace('\xe7',"c").replace('\xde',"s").replace('\xfe',"s").replace('\xc7',"c").replace('\xf0',"g")
        response.close()

                        
        you_match=re.compile('src="http\:.*?youtube.com/embed/(.*?)"').findall(link)
        print you_match
        for code in you_match:
                print code
                yt=('plugin://plugin.video.youtube/?action=play_video&videoid='+str(code))
                araclar.addLink('[Film Bitti ~ ]',yt,'')
                playList.add(yt)

        
                xbmcPlayer.play(playList)
        

