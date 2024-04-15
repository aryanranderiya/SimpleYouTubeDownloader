from pytube import YouTube
from pytube import Playlist
from pathlib import Path
import os
import sys

downloads_path = str(Path.home() / "Desktop")
filesize = ""


def download_video(link: str) -> None:
    yt = YouTube(link)
    print(f'Downloading: {yt.title}')
    yt.register_on_progress_callback(on_progress)

    folder_name = "".join(x for x in yt.title if (x.isalnum() or x in "._- "))
    directory: str = f"{downloads_path}/{folder_name}"
    os.makedirs(directory, exist_ok=True)

    stream = yt.streams.get_by_itag(137)
    stream.download(output_path=directory)

    print(f"Video {yt.title} Downloaded at {directory}!")


def download_playlist(link: str) -> None:
    p = Playlist(link)
    print(f'Downloading Playlist: {p.title}')

    folder_name = "".join(x for x in p.title if (x.isalnum() or x in "._- "))
    directory: str = f"{downloads_path}/{folder_name}"
    os.makedirs(directory, exist_ok=True)

    for index, video in enumerate(p.videos, start=1):
        print(f'Downloading Video: "{video.title}" {index}/{p.length}')
        video.register_on_progress_callback(on_progress)
        video.streams.first().download(output_path=directory, )

    print(f"Playlist {p.title} Downloaded at {directory}!")


def on_progress(stream, chunk, bytes_remaining) -> None:
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = int(bytes_downloaded / total_size * 100)
    print(f"""{percentage}% : {
          bytes_downloaded}/{total_size} Chunks Downloaded""", flush=True)


def main() -> None:
    link: str = input("Enter YouTube Link: (Video or Playlist)")

    if "playlist" in link:
        download_playlist(link)
    else:
        download_video(link)


if __name__ == "__main__":
    main()
