import sys
import os
import yt_dlp
from pydub import AudioSegment



def download_and_convert(singer, n):
    os.makedirs("audios", exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "audios/audio%(id)s.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    search_url = f"ytsearch{n}:{singer}"
    audio_paths = []

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_url, download=True)

        for entry in info["entries"]:
            filename = f"audios/audio{entry['id']}.mp3"
            audio_paths.append(filename)

    return audio_paths



def cut_audios(audio_paths, duration):
    os.makedirs("cuts", exist_ok=True)
    cut_paths = []

    for i, path in enumerate(audio_paths):
        sound = AudioSegment.from_file(path)
        cut = sound[: duration * 1000]
        out = f"cuts/cut{i}.mp3"
        cut.export(out, format="mp3")
        cut_paths.append(out)

    return cut_paths


def merge_audios(cut_paths, output):
    final = AudioSegment.empty()

    for path in cut_paths:
        final += AudioSegment.from_file(path)

    final.export(output, format="mp3")



def main():
    if len(sys.argv) != 5:
        print("Usage: python <file.py> <Singer> <NoVideos> <DurationSec> <OutputFile>")
        return

    singer = sys.argv[1]
    n = int(sys.argv[2])
    duration = int(sys.argv[3])
    output = sys.argv[4]

    try:
        print("Downloading & converting to MP3...")
        audios = download_and_convert(singer, n)

        print("Cutting audio...")
        cuts = cut_audios(audios, duration)

        print("Merging...")
        merge_audios(cuts, output)

        print("\n Mashup created successfully!")
        print("Output file:", output)

    except Exception as e:
        print(" Error:", e)


if __name__ == "__main__":
    main()
