from flask import Flask, render_template, make_response, jsonify, request, redirect
from flask.helpers import url_for
from os import getcwd, path
import core

import index.modele
import administration.modele

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Asecret'
bdd_location = path.join(getcwd(), "scrapper_scan-manga.com.sqlite")

@app.route("/", methods=["GET"])
def home_page() -> str:
    return render_template("index.html")


@app.route("/getData", methods=["GET"])
def getData() -> None:
    
    data = index.modele.get_new_episode(bdd_location)
    return make_response(jsonify(data), 200)



@app.route("/administration", methods=["GET"])
def admin() -> None:
    return render_template("administration.html", 
                            series = administration.modele.get_all_short(bdd_location)
)  


@app.route("/addSerie", methods=["POST"])
def addSerie() -> None:
    url   = request.form.get("url")
    short = request.form.get("short")
    
    if url == None or short == None:
        return make_response(render_template("error.html", message="missing argument"), 400)
    
    if not administration.modele.add_serie(bdd_location, url, short):
        return make_response(render_template("error.html", message="request process error"), 500)

    return redirect(url_for("admin"))


@app.route("/deleteSerie", methods=["POST"])
def deleteSerie() -> None:
    
    serie_to_delete  = request.form.getlist("series_to_delete")
    
    if not serie_to_delete:
        return make_response(render_template("error.html", message="missing argument"), 400)

    administration.modele.del_serie(bdd_location, tuple(serie_to_delete))
    return redirect(url_for("admin"))
 

if __name__ == "__main__":
    core.modele.init_bdd(bdd_location)
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8080)
   