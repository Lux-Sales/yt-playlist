import os
import subprocess

from pytube import Playlist, YouTube

def run():
    pl_str = input("Enter playlist url: ")
    pl = Playlist(pl_str)
    # get parent directory; VERY IMPORTANT!!
    # INCLUDE LAST SLASH AFTER FOLDER NAME
    # e.g. /home/username/Folder/ or C:\Users\Username\Folder\
    filepath = '/musicas'
    # get linked list of links in the playlist
    links = pl.video_urls
    # download each item in the list
    faileds = []
    for l in links:
        try:
            # converts the link to a YouTube object
            yt = YouTube(l)
            # takes first stream; since ffmpeg will convert to mp3 anyway
            music = yt.streams.first()
            # gets the filename of the first audio stream
            default_filename = music.default_filename
            print("Downloading " + default_filename + "...")
            # downloads first audio stream
            music.download()
            # creates mp3 filename for downloaded file
            new_filename = default_filename[0:-3] + "mp3"
            print("Converting to mp3....")
            # converts mp4 audio to mp3 audio
            subprocess.run(['ffmpeg', '-i', 
                os.path.join(filepath, default_filename),
                os.path.join(filepath, new_filename)
            ])
        except Exception:
            faileds.append(new_filename)
            continue
    print("Download finished.")
    print("Fails:\n")
    for fail in faileds:
        print(fail + '\n')
    
run()