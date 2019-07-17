from Spiders.API_music import musicAPI
import re
import requests

class Songinfo(object):
    songName=''
    songUrl=''
    musicAPI=musicAPI()
    def __init__(self,url):
        self.findSongUrl(url)
    def findSongUrl(self,url):
        if 'music.163' in url:
            print('此链接为网易云音乐')
            search1 = re.search(r'[a-z].+\&', url, re.I)
            if search1 == None:
                # print('此音乐下载地址为:' + get_music_cloud163(url))
                # exit()
                downloadUrl = musicAPI.get_music_cloud163(url)
                self.setSongUrl(downloadUrl)
            else:
                url = search1.group(0).replace('&', '')
                # print('此音乐下载地址为:' + get_music_cloud163(url))
                # exit()
                downloadUrl = musicAPI.get_music_cloud163(url)
                self.setSongUrl(downloadUrl)
        if 'qq.com' in url:
            print('此链接为QQ音乐')
            obj = re.search(r'(?<=songid=)\d+', url, re.I)  # 预见匹配
            if(obj==None):
                songid = url.rsplit('/', 1)[1]
                songid = songid.rsplit('.', 1)[0]
                html = requests.get(url)
                search = re.findall(r'<h1.*?>(.*?)</h1>', html.text, re.I)
                print(search[1])
                downloadUrl=musicAPI.get_music_qq('0',songid)
                self.setSongUrl(downloadUrl)
            else:
                downloadUrl=musicAPI.get_music_qq(url,'0')
                self.setSongUrl(downloadUrl)
            # print('此音乐下载地址为:' + xs)
            # exit()
        if 'taihe.com' in url:
            print('此链接为千千(百度)音乐')
            # print('此音乐下载地址为:' + get_music_qianqian(url))
            # exit()
            downloadUrl = musicAPI.get_music_qianqian(url)
            self.setSongUrl(downloadUrl)
        if 'kuwo.cn' in url:
            print('此链接为酷我音乐')
            # print('此音乐下载地址为:' + get_music_kuwo(url))
            # exit()
            downloadUrl = musicAPI.get_music_kuwo(url)
            self.setSongUrl(downloadUrl)
        if '1ting.com' in url:
            print('此链接为一听音乐')
            # print('此音乐下载地址为:' + get_music_1ting(url))
            # exit()
            downloadUrl = musicAPI.get_music_1ting(url)
            self.setSongUrl(downloadUrl)
        if '5sing.kugou' in url:
            print('此链接为5sing音乐')
            # print('此音乐下载地址为:' + get_music_5sing(url))
            # exit()
            downloadUrl = musicAPI.get_music_5sing(url)
            self.setSongUrl(downloadUrl)
        if 'yue365.com' in url:
            print('此链接为365音乐')
            # print('此音乐下载地址为:' + get_music_365(url))
            # exit()
            downloadUrl = musicAPI.get_music_365(url)
            self.setSongUrl(downloadUrl)
        if 'changba.com' in url:
            print('此链接为唱吧音乐')
            # print('此音乐下载地址为:' + get_music_changba(url))
            # exit()
            downloadUrl = musicAPI.get_music_changba(url)
            self.setSongUrl(downloadUrl)

        if '9sky.com' in url:
            print('此链接为九天音乐')
            # print('此音乐下载地址为:' + get_music_jiutian(url))
            # exit()
            downloadUrl = musicAPI.get_music_jiutian(url)
            self.setSongUrl(downloadUrl)

        if 'lizhi.fm' in url:
            print('此链接为荔枝FM')
            # print('此音乐下载地址为:' + get_music_lizhifm(url))
            # exit()
            downloadUrl = musicAPI.get_music_lizhifm(url)
            self.setSongUrl(downloadUrl)
        if 'app-echo.com' in url:
            print('此链接为echo回声')
            downloadUrl = musicAPI.get_music_echo(url)
            self.setSongUrl(downloadUrl)
        else:
            return 0
    def setSongName(self,name):
        self.songName=name

    def setSongUrl(self, url):
        self.songUrl = url
    def getSongName(self):
        return self.songName
    def getSongUrl(self):
        return self.songUrl

