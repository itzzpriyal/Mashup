from flask import Flask, request, render_template_string
import zipfile
import yagmail
import os
import subprocess

app = Flask(__name__)

HTML = """
<h2>Mashup Generator</h2>
<form method="post">
Singer Name: <input name="singer" required><br><br>
Number of Videos: <input name="n" required><br><br>
Duration (seconds): <input name="d" required><br><br>
Your Email: <input name="email" required><br><br>
<button type="submit">Create Mashup</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form["singer"]
        n = request.form["n"]
        d = request.form["d"]
        email = request.form["email"]

        output = "output.mp3"

       
        subprocess.run(
            ["python", "../program1/102303563.py", singer, n, d, output],
            check=True
        )

       
        zip_name = "mashup.zip"
        with zipfile.ZipFile(zip_name, "w") as z:
            z.write(output)

       
        yag = yagmail.SMTP("pgupta4_be23@thapar.edu", "wxyl wkln ftso swip")
        yag.send(email, "Your Mashup File", "Attached is your mashup 🎵", [zip_name])

        return "<h3>Email sent successfully!</h3>"

    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)
