#Kütüphaneyi indirmek için --> pip install youtube_dl


import youtube_dl
import time

video_url = input ("Link giriniz:")

video_bilgisi = youtube_dl.YoutubeDL().extract_info(
    url = video_url,download=False)

dosya_adi = f"{video_bilgisi['title']}.mp3"

ayarlar = {
    'format':'bestaudio',
    'keepvideo': False,
    'output':dosya_adi,
    }

with youtube_dl.YoutubeDL(ayarlar) as ydl:
    ydl.download([video_bilgisi['webpage_url']])

print (f"İndirme Tamamlandı... (coded by iboow37) || --> {dosya_adi}")
time.sleep (3)
input("ENTER tuşuna basarak çıkış yapabilirsiniz...")

