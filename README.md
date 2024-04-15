Here's a README.md for your script:

---

# YouTube Downloader

This script allows you to download either single YouTube videos or entire playlists.

## Requirements

- Python 3.x
- [pytube](https://github.com/pytube/pytube)

## Installation

1. Clone or download this repository.
2. Install the required dependencies:

```bash
pip install pytube
```

## Usage

1. Run the script:

```bash
python youtube_downloader.py
```

2. Enter the YouTube link of the video or playlist you want to download when prompted.

## Features

- Downloads single YouTube videos.
- Downloads entire YouTube playlists.

## How it Works

1. The script prompts you to enter a YouTube link.
2. It detects whether the link is for a single video or a playlist.
3. For a single video, it downloads the highest quality available.
4. For a playlist, it downloads all the videos in the playlist.
5. Progress of each download is displayed.

## Example

```python
python youtube_downloader.py
```

```
Enter YouTube Link: (Video or Playlist) <Enter your YouTube link here>
```

## Note

- The downloaded videos are saved in a new folder with the Playlist/Video title on your desktop by default.

---
