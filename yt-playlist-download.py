import traceback
import os
from pytube import Playlist, YouTube

def run():
    pl_str = "https://www.youtube.com/playlist?list=PLv1AVL714MdVNABdWUu9FY19W6jz0eZSC"
    pl = Playlist(pl_str)
    # get parent directory; VERY IMPORTANT!!
    # INCLUDE LAST SLASH AFTER FOLDER NAME
    # get linked list of links in the playlist
    links = pl.video_urls
    # download each item in the list
    faileds = []
    musics_downloaded = os.listdir('/home/lucas/musicas/yt-playlist/musicas')
    for l in links:
        try:
            # converts the link to a YouTube object
            yt = YouTube(l)
            # takes first stream; since ffmpeg will convert to mp3 anyway
            music = yt.streams.first()
            # gets the filename of the first audio stream
            if not music.default_filename.replace(".mp3", ".3gpp") in musics_downloaded:
                print("Downloading " + music.default_filename + "...")
                # downloads first audio stream
                music.download()
                filename = music.default_filename.replace(".3gpp", ".mp3")
                os.rename(music.default_filename, filename)
            else:
                continue
        except Exception:
            print(traceback.format_exc())
            faileds.append(music.default_filename)
            continue
    print("Download finished.")
    print("Fails:\n")
    for fail in faileds:
        print(fail + '\n')
    
run()