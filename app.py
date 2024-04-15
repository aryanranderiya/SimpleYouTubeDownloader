from pytube import YouTube
from pytube import Playlist
from pathlib import Path
import os
import sys
import threading

# downloads_path = str(Path.home() / "Desktop")
downloads_path = r"E:\AryanRanderiyaPC\PCHDDLibraries\Videos"
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


def download_p_video(video, directory):
    video.streams.first().download(output_path=directory)


def download_playlist(link: str) -> None:
    p = Playlist(link)
    print(f'Downloading Playlist: {p.title}')

    folder_name = "".join(x for x in p.title if (x.isalnum() or x in "._- "))
    directory: str = f"{downloads_path}/{folder_name}"
    os.makedirs(directory, exist_ok=True)

    threads = []

    for index, video in enumerate(p.videos, start=1):
        vid_number: str = f"{index}/{p.length}  "
        print(f'Downloading Video {vid_number} : "{video.title}"')

        video.register_on_progress_callback(lambda stream, chunk, bytes_remaining, title=vid_number+video.title:
                                            on_progress(stream, chunk, bytes_remaining, title))

        thread = threading.Thread(
            target=download_p_video, args=(video, directory))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"Playlist {p.title} Downloaded at {directory}!")


def on_progress(stream, chunk, bytes_remaining, title) -> None:
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = int(bytes_downloaded / total_size * 100)
    print(f"""{title} : {percentage}% : {
          bytes_downloaded}/{total_size} Chunks Downloaded""", flush=True)


def main() -> None:
    link: str = input("Enter YouTube Link: (Video or Playlist): ")

    if "playlist" in link:
        download_playlist(link)
    else:
        download_video(link)


if __name__ == "__main__":
    main()
