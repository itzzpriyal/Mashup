🎵 Mashup Generator – Python Project

A Python-based mashup generator that downloads songs from YouTube, converts them into audio, trims a specified duration from each clip, merges all clips into a single MP3 mashup, and delivers the result through a Flask web application with automated ZIP creation and email sending.

🚀 Features

Download songs of any singer from YouTube

Convert downloaded media into MP3 audio

Trim the first Y seconds from each audio clip

Merge multiple clips into one mashup file

Simple web interface using Flask

Automatic ZIP creation and email delivery to the user

🛠️ Technologies Used

Python 3.11

yt-dlp – YouTube media downloading

pydub – audio trimming and merging

FFmpeg – media processing backend

Flask – web application framework

yagmail – automated email sending

📁 Project Structure

mashup/
│
├── program1/
│ └── 102303563.py – Command-line mashup generator
│
├── program2/
│ └── app.py – Flask web application
│
└── README.md

▶️ Running Program 1 (Command Line Mashup)

Run the following command inside the program1 folder:

python 102303563.py "Singer Name" <NumberOfVideos> <DurationSeconds> output.mp3

Example:

python 102303563.py "Diljit Dosanjh" 10 20 output.mp3

This process downloads songs from YouTube, converts them into MP3 audio, trims the specified duration from each clip, and merges all clips into a single output.mp3 mashup file.

🌐 Running Program 2 (Web Application)

Navigate to the program2 folder and run:

python app.py

Then open a browser and visit:

http://127.0.0.1:5000

Enter the singer name, number of videos, clip duration, and your email address.
After submission, the mashup is generated, compressed into a ZIP file, and sent to the provided email.

🔐 Email Configuration

To enable email sending, first enable 2-Step Verification in your Google account, then generate a Gmail App Password.
Update the credentials inside app.py using your email and the generated app password so that the application can send the mashup ZIP file automatically.

🎯 Academic Objective

This project demonstrates Python automation, media downloading and processing, audio manipulation, Flask-based web development, and automated email delivery.
It fulfills the requirements of the Mashup Assignment by integrating command-line processing with a web-based user interface.

👩‍💻 Author

Priyal Gupta
B.Tech Student – Computer Science

📜 License

This project is developed strictly for educational and academic purposes only.
