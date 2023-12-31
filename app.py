from flask import Flask, render_template, request, redirect, url_for
import json, requests

app = Flask(__name__)
ap = "https://api.edamam.com/api/recipes/v2"
parameters = {
    "app_id": "1cd6db20",
    "app_key": "6dabaa16f7dd84c2501b48f31475bc74",
    "type": "public"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(url_for("search_query"))
    
    parameters["random"] = "true"
    parameters["mealType"] = "breakfast"
    breakfast = json.loads(requests.get(ap, params=parameters).text)
    parameters["mealType"] = "dinner"
    dinner = json.loads(requests.get(ap, params=parameters).text)
    parameters["mealType"] = "snack"
    snack = json.loads(requests.get(ap, params=parameters).text)
    return render_template("index.html", title="Home", breakfast=breakfast, dinner=dinner, snack=snack)

@app.route("/search")
def search_query():
    parameters["q"] = request.args.get('query')
    parameters.pop("mealType", None)
    parameters.pop("random", None)
    results = json.loads(requests.get(ap, params=parameters).text)
    return render_template("search.html", title="Search", results=results, query=parameters["q"])
    
if __name__ == "__main__":
    app.run(debug=True)
