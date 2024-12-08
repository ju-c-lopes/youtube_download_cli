import os
from time import sleep

import colorama
from colorama import Fore
from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress

colorama.init(autoreset=True)

link = input("Enter the playlist: ")
playlist = Playlist(link)
title = playlist.title
os.system(f"mkdir ./Downloads/'{title}'")

i = 0

for link_video in playlist.video_urls:
    try:
        video = YouTube(link_video, on_progress_callback=on_progress)
        print(Fore.RED + "\nDownloading => " + Fore.BLUE + f"{video.title}")
        video.streams.get_highest_resolution().download(output_path=f"./Downloads/{title}")
    except Exception:
        print("It was impossible to download this video")
        sleep(3)
        continue
    sleep(3)
    print(Fore.GREEN + "Download completed!!\n")
    print(str(i + 1) + " ok")
    i += 1
