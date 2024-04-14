import os
import re
import requests
import asyncio
from pytube import YouTube
from TikTokApi import TikTokApi

def sanitize_filename(name):
    """Sanitize filenames to avoid issues on different OS."""
    return re.sub(r'[^a-zA-Z0-9_\-. ]', '', name)

def download_youtube_short(link):
    try:
        yt = YouTube(link)
        video_title = sanitize_filename(yt.title)
        video_stream = yt.streams.get_highest_resolution()
        print(f"Downloading YouTube Short: {video_title}")
        video_stream.download(filename=f"{video_title}.mp4")
        print(f"Download completed: {video_title}")
    except Exception as e:
        print(f"Error downloading YouTube Short: {link}")
        print(str(e))

async def download_tiktok_video(link):
    ms_token = os.environ.get("ms_token", None)  # Ensure you set your MS token environment variable
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        video = api.video(url=link)
        video_info = await video.info()  # Get video information
        video_title = sanitize_filename(video_info["desc"])
        video_url = video_info["video"]["downloadAddr"]
        print(f"Downloading TikTok video: {video_title}")
        video_content = requests.get(video_url).content  # Synchronous request to download the video
        with open(f"{video_title}.mp4", "wb") as file:
            file.write(video_content)
        print(f"Download completed: {video_title}")

async def download_videos(video_links):
    for link in video_links:
        if "youtube.com" in link or "youtu.be" in link:
            download_youtube_short(link)
        elif "tiktok.com" in link:
            await download_tiktok_video(link)
        else:
            print(f"Unsupported video link: {link}")

if __name__ == "__main__":
    video_links = []
    print("Enter video links (YouTube Shorts or TikTok) (press Enter without input to finish):")
    while True:
        link = input()
        if not link:
            break
        video_links.append(link)

    asyncio.run(download_videos(video_links))
    print("All videos downloaded successfully!")