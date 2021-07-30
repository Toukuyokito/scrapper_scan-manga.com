from flask import Flask, render_template, make_response, jsonify, request, redirect
from flask.helpers import url_for

import modele_get
import modele_core
import modele_post
import modele_delete


app = Flask(__name__)
app.config['SECRET_KEY'] = 'A secret \U0001F92B'
bdd_location = "scrapper_scan-manga.com.sqlite"

@app.route("/", methods=["GET"])
def index() -> str:
    return render_template("index.html")


@app.route("/administration", methods=["GET"])
def administration() -> None:
    return render_template("administration.html", 
                            series = modele_get.all_short(bdd_location)
)  


@app.route("/getData", methods=["GET"])
def getData() -> None:
    
    data = modele_get.new_episode(bdd_location)
    print(data)
    return make_response(jsonify(data), 200)


@app.route("/addSerie", methods=["POST"])
def addSerie() -> None:
    url   = request.form.get("url")
    short = request.form.get("short")
    
    if url == None or short == None:
        return make_response(render_template("error.html", message="missing argument"), 400)
    
    if not modele_post.add_serie(bdd_location, url, short):
        return make_response(render_template("error.html", message="request process error"), 500)

    return redirect(url_for("administration"))


@app.route("/deleteSerie", methods=["POST"])
def deleteSerie() -> None:
    
    serie_to_delete  = request.form.getlist("series_to_delete")
    
    if not serie_to_delete:
        return make_response(render_template("error.html", message="missing argument"), 400)

    modele_delete.del_serie(bdd_location, tuple(serie_to_delete))
    return redirect(url_for("administration"))


if __name__ == "__main__":

    modele_core.init_bdd(bdd_location)
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8080)
    