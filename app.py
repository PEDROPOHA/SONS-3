from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# rota principal
@app.route("/")
def index():
    return render_template("index.html")

# rota para download
@app.route("/download/<filename>")
def download(filename):
    music_dir = os.path.join(app.root_path, "static/musicas")
    return send_from_directory(music_dir, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)