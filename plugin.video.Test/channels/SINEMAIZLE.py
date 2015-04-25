# -*- coding: utf-8 -*-
import xbmcplugin,xbmcgui,xbmcaddon,xbmc,urllib,urllib2,os,sys,re
import araclar,cozucu


Addon = xbmcaddon.Addon('plugin.video.Test')
__settings__ = xbmcaddon.Addon(id='plugin.video.Test')
__language__ = __settings__.getLocalizedString


fileName ="SINEMAIZLE"
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)


############# ANA GIRIS KLASORLERI ##############################
def main():
        url='http://www.sinemadafilmizle.com/'
        #araclar.addDir(fileName,name,"mode(name,url)",url,thumbnail)
        araclar.addDir(fileName,'[COLOR red][B]>>>>>>>>>>>>>>>>>[/B][/COLOR][COLOR yellow][B] Film ARA - SEARCH[/B][/COLOR][COLOR red][B] <<<<<<<<<<<<<<<<<[/B][/COLOR]', "Search()", "","special://home/addons/plugin.video.Test/resources/images/ARAMA_SEARCH.png")
        araclar.addDir(fileName,'[COLOR blue][B]>> [/B][/COLOR][COLOR lightblue][B]Yeni Eklenen Filmler [/B][/COLOR]', "Yeni(url)",url,"http://www.filmizletir.net/wp-content/uploads/2012/10/logo7.png" )
                ##### KATEGORILERI OKU EKLE ##########################
        
        link=araclar.get_url(url)
        match=re.compile('class="cat-item cat-item-.*?"><a href="(.*?)" title=".*?"(.*?)</a>').findall(link)
        for url,name in match:               
                araclar.addDir(fileName,'[COLOR orange][B]>> [/B][/COLOR]'+'[COLOR beige][B]' + name+'[/B][/COLOR]',"Yeni(url)",url,"")

###################################################################                

                                                
######                       
def Search():
        keyboard = xbmc.Keyboard("", 'Search', False)
        keyboard.doModal()
        if keyboard.isConfirmed():
            query = keyboard.getText()
            query=query.replace(' ','+')
            url = ('http://www.sinemadafilmizle.com/index.php?s='+query)
            Yeni(url)

############
def Yeni(url):
        link=araclar.get_url(url)  
        match=re.compile('<a href="(.*?)" title=".*?">\n<div class=".*?"></div><img src="(.*?)" alt="(.*?)" />\n</a>\n').findall(link)
        for url,thumbnail,name in match:
                araclar.addDir(fileName,'[COLOR lightgreen][B]'+name+'[/B][/COLOR]',"VIDEOLINKS(name,url)",url,thumbnail)

        page=re.compile('<a href=\'(.*?)\' class=\'page larger\'>(.*?)</a>').findall(link)
        
        for url,name in page:
                araclar.addDir(fileName,'[COLOR purple][B]>>SAYFA-' + name+'[/B][/COLOR]',"Yeni(url)",url,"special://home/addons/plugin.video.Test/resources/images/sonrakisayfa.png")                     
        
###########        


        
#############
def VIDEOLINKS(name,url):
        #---------------------------#
        urlList=[]
        #---------------------------#
        playList.clear()
        link=araclar.get_url(url)
        vk_1=re.compile('src="http://vk.com/(.*?)"').findall(link)
        for url in vk_1:
                url = 'http://vk.com/'+str(url)
                url=url.strip(' \t\n\r').replace("&amp;","&").replace("?rel=0","").replace(";=","=")
                #-----------------------#
                urlList.append(url)
                #-----------------------#
        try:
                code=re.match(r"http://www.youtube.com/embed/(.*?)$", url).group(1)
                url='plugin://plugin.video.youtube/?action=play_video&videoid=' + str(code)
                urlList.append(url)
        except:
                pass
        if not urlList:
                match=re.compile('<li><h1><a  href="(.*?)"').findall(link)
                print match
                if match:
                        for url in match:
                                VIDEOLINKS(name,url)
       
        if urlList:
                dialog = xbmcgui.Dialog()
                karar=("izle","indir- Henuz yapılmadı")
                ret = dialog.select(__language__(30008),karar)
        
                if ret == 0:
                        Sonuc=cozucu.videobul(urlList)
                        if Sonuc=="False":
                                dialog = xbmcgui.Dialog()
                                i = dialog.ok(name,"Site uyarisi","     Film Siteye henuz yuklenmedi   ","  Yayinlandiktan sonra yüklenecektir.  ")
                                return False 
                        else:                                
                                for name,url in Sonuc if not isinstance(Sonuc, basestring) else [Sonuc]:
                                                araclar.addLink(name,url,'')
                                                araclar.playlist_yap(playList,name,url) 
                                xbmcPlayer.play(playList)

                if ret == 1:
                        Sonuc=cozucu.videobul(urlList)
                        urlList=[]
                        for isim,new_url in Sonuc if not isinstance(Sonuc, basestring) else [Sonuc]:
                                urlList.append(new_url)  
                        araclar.indir(isim,urlList)
        else:
             return araclar.hata()
    
             
        

