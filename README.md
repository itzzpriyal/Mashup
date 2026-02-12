# 🎵 Mashup Generator

Mashup Generator is a Python-based multimedia automation project that creates a single audio mashup by downloading songs from YouTube, converting them into MP3 format, trimming a fixed duration from each track, and seamlessly merging the processed clips into one final output file. In addition to command-line execution, the project includes a lightweight Flask web interface that allows users to generate mashups, package the result as a ZIP file, and receive it through automated email delivery.

## ✨ Features
- Automated YouTube song downloading using **yt-dlp**
- Audio conversion, trimming, and merging powered by **pydub** and **FFmpeg**
- Configurable number of tracks and clip duration
- Command-line based mashup generation workflow
- Simple **Flask web interface** for user interaction
- Automatic **ZIP creation and email sharing** of the generated mashup

## 🛠️ Tech Stack
**Python 3.11** · yt-dlp · pydub · FFmpeg · Flask · yagmail

## 📁 Project Structure
- **program1/** – Core logic for downloading, processing, and merging audio  
- **program2/** – Web application for mashup generation and email delivery  

## 🎯 Objective
This project was developed as part of an academic assignment to demonstrate real-world application of Python scripting, multimedia processing, web development, and automation. It showcases how multiple technologies can be integrated to build a complete end-to-end system for content processing and distribution.

## 👩‍💻 Author
**Priyal Gupta**
