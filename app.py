from flask import Flask, render_template


# membuat aplikasi Flask
app = Flask(__name__)


# halaman utama
@app.route("/")
def home():
    return render_template("index.html")


# menjalankan website
if __name__ == "__main__":
    app.run(debug=True)