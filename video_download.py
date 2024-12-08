import colorama
from colorama import Fore
from pytubefix import YouTube
from pytubefix.cli import on_progress

colorama.init(autoreset=True)

link = input("Enter the link: ")
youtube_video_to_download = YouTube(link, on_progress_callback=on_progress)

# Showing details
print("Title: ", youtube_video_to_download.title)

cancel = 0
while True:
    try:
        if cancel > 2:
            cancel_confirm = input("Deseja cancelar? Y/N ")
            cancel_confirm = cancel_confirm.lower()

            while cancel_confirm != "y" and cancel_confirm != "n":
                cancel_confirm = input("Deseja cancelar? Y/N ")
                cancel_confirm = cancel_confirm.lower()
            if cancel_confirm == "y":
                print("Cancelado com sucesso\n")
                break

        youtube_stream = youtube_video_to_download.streams.get_highest_resolution()

        # Starting download
        print(Fore.RED + "\nDownloading...")
        youtube_stream.download(output_path="./Downloads")
        print(Fore.GREEN + "Download completed!!\n")
        break
    except Exception:
        print("Your choice doesn't exists")
    cancel += 1
