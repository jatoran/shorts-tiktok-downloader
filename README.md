# shorts-tiktok-downloader

# YouTube Shorts and TikTok Video Downloader

This Python script allows you to download YouTube Shorts and TikTok videos by providing a list of video links. It utilizes the `pytube` library for downloading YouTube Shorts and the `TikTokApi` library for downloading TikTok videos.

## Features

- Download YouTube Shorts videos by providing the video links
- Download TikTok videos by providing the video links
- Supports downloading multiple videos at once
- Automatically sanitizes the video titles to create valid filenames

## Prerequisites

- Python 3.6 or above (asyncio is part of the standard library from Python 3.6 onwards)
- `pytube` library
- `TikTokApi` library
- `requests` library

## Installation

1. Clone the repository or download the script file.

2. Install the required libraries using pip:
```
pip install pytube TikTokApi
```

## Usage

1. Run the script using Python:
```
python video_downloader.py
```

3. Enter the YouTube Shorts and TikTok video links when prompted. Press Enter without entering a link to finish the input.

4. The script will download each video and save it in the current directory with the sanitized video title as the filename.

5. After all the videos are downloaded, the script will display a success message.

## Examples

Here's an example of how to use the video downloader script:
```
Enter video links (YouTube Shorts or TikTok) (press Enter without input to finish):
https://www.youtube.com/shorts/abc123
https://www.tiktok.com/@username/video/123456
https://www.youtube.com/shorts/def456

Downloading YouTube Short: Cool_Video_Title
Download completed: Cool_Video_Title
Downloading TikTok video: Awesome_TikTok_Video
Download completed: Awesome_TikTok_Video
Downloading YouTube Short: Another_Great_Video
Download completed: Another_Great_Video
All videos downloaded successfully!
```

In this example, the user enters three video links (two YouTube Shorts and one TikTok video). The script downloads each video and saves it with the sanitized video title as the filename. Finally, it displays a success message.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

Please note that downloading videos from YouTube and TikTok may be subject to their respective terms of service and copyright policies. Make sure you have the necessary permissions and comply with the platforms' guidelines when using this script.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
