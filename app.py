from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pendidikan")
def pendidikan():
    return render_template("pendidikan.html")


@app.route("/pengalaman")
def pengalaman():
    return render_template("pengalaman.html")


@app.route("/project")
def project():
    return render_template("project.html")



if __name__=="__main__":
    app.run(debug=True)