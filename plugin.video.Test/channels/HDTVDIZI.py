# -*- coding: utf-8 -*-
import xbmcplugin,xbmcgui,xbmcaddon,xbmc,urllib,urllib2,os,sys,re
import araclar,cozucu


Addon = xbmcaddon.Addon('plugin.video.Test')
__settings__ = xbmcaddon.Addon(id='plugin.video.Test')
__language__ = __settings__.getLocalizedString


fileName ="HDTVDIZI"
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)


############# ANA GIRIS KLASORLERI ##############################
def main():
        url='http://www.hdtvdiziizle.com/'
        #araclar.addDir(fileName,name,"mode(name,url)",url,thumbnail)
        araclar.addDir(fileName,'[COLOR red][B]>>>>>>>>>>>>>>>>>[/B][/COLOR][COLOR yellow][B] Film ARA - SEARCH[/B][/COLOR][COLOR red][B] <<<<<<<<<<<<<<<<<[/B][/COLOR]', "Search()", "","special://home/addons/plugin.video.Test/resources/images/ARAMA_SEARCH.png")
##        araclar.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR][COLOR lightblue][B] Yabanci Diziler [/B][/COLOR]', "Yeni(url)",url,"special://home/addons/plugin.video.Test/resources/images/yeni.png" )
##        araclar.addDir(fileName,'[COLOR blue][B]>>[/B][/COLOR][COLOR lightblue][B] Yerli Diziler [/B][/COLOR]', "Yeni(url)",url,"special://home/addons/plugin.video.Test/resources/images/yeni.png" )
##        #araclar.addDir(fileName,'[COLOR red][B]>>[/B][/COLOR][COLOR pink][B] Editorun Sectikleri [/B][/COLOR]', "Edit(url)",url,"")
##        araclar.addDir(fileName,'[COLOR gold][B]>>[/B][/COLOR][COLOR beige][B] Turkce Dublaj Filmler [/B][/COLOR]', "Dublaj(url)","http://www.baglanfilmizle.com/film-izle/izleme-secenekleri/turkce-dublaj","")
##        araclar.addDir(fileName,'[COLOR green][B]>>[/B][/COLOR][COLOR lightgreen][B] Yerli Filmler [/B][/COLOR]', "Yerli(url)","http://www.baglanfilmizle.com/film-izle/yerli-filmler)","")
##        ##### KATEGORILERI OKU EKLE ##########################
        
        link=araclar.get_url(url)
        match=re.compile('<li id="menu-item-.*?" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.*?"><a href="(.*?)">(.*?)</a>').findall(link)
        for url,name in match:
                araclar.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR][COLOR beige][B]'+ name+'[/B][/COLOR]',"Yeni(url)",url,"")

###################################################################                

                                                
######                       
def Search():
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            query=query.replace(' ','+')
            url = ('http://www.hdtvdiziizle.com/?s='+query)
            Yeni(url)

############
def Yeni(url):
        link=araclar.get_url(url)  
        match=re.compile('<a href="(.*?)" rel="bookmark" title=".*?"><img src="(.*?)" alt="(.*?)" /></a>').findall(link)
        for url,thumbnail,name in match:
                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail)

        page=re.compile('class="active_page"><a href="http://www.hdtvdiziizle.com/category.*?">.*?</a></li>\n<li><a href="(.*?)">(.*?)</a>').findall(link)
        
        for url,name in page:
                araclar.addDir(fileName,'[COLOR purple][B]>>SAYFA-' + name+'[/B][/COLOR]',"Yeni(url)",url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")                     
        
###########        
##def session(url):
##        link=araclar.get_url(url)       
##        match=re.compile('<a href="(.*?)" title="(.*?)">.*?</a>\n<div class="film-sosyal">').findall(link)
##        for url,name in match:
##                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,'')
##
##        page=re.compile('class=\'current\'>.*?</span><a href=\'(.*?)\' class=\'page larger\'>(.*?)</a>').findall(link)
##        
##        for url,name in page:
##                araclar.addDir(fileName,'[COLOR purple][B]>>SAYFA-' + name+'[/B][/COLOR]',"session(url)",url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")                     
##                                   
##    

        
#############
def VIDEOLINKS(name,url):
        playList.clear()
        link=araclar.get_url(url)
        match=re.compile('src="http://vk.com/(.*?)"').findall(link)
        for url in match:
                url='http://vk.com/'+url
                Sonuc=cozucu.videobul(url)
                print "donen sonuc",Sonuc
                if Sonuc=="False":
                        dialog = xbmcgui.Dialog()
                        i = dialog.ok(name,"Site uyarisi","     Film Siteye henuz yuklenmedi   ","  Yayinlandiktan sonra yüklenecektir.  ")
                        return False 
                else:                                
                        for name,url in Sonuc if not isinstance(Sonuc, basestring) else [Sonuc]:
                                        araclar.addLink(name,url,'')
                                        araclar.playlist_yap(playList,name,url) 
                        xbmcPlayer.play(playList)

                        
        link=araclar.get_url(url)
        match=re.compile('src="http://www.youtube.com/embed/(.*?)"').findall(link)
        print match
        for url in match:
                url='http://www.youtube.com/embed/'+url
                print url
                Sonuc=cozucu.videobul(url)
                print "donen sonuc",Sonuc
                if Sonuc=="False":
                        dialog = xbmcgui.Dialog()
                        i = dialog.ok(name,"Site uyarisi","     Film Siteye henuz yuklenmedi   ","  Yayinlandiktan sonra yüklenecektir.  ")
                        return False 
                else:                                
                        for name,url in Sonuc if not isinstance(Sonuc, basestring) else [Sonuc]:
                                        araclar.addLink(name,url,'')
                                        araclar.playlist_yap(playList,name,url) 
                        xbmcPlayer.play(playList)
        
             
        

