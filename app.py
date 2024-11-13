from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pizzas = [
    {"name": "Маргарита", "ingredients": "Томатний соус, моцарела, базилік", "price": 190},
    {"name": "Гавайська", "ingredients": "Соус, моцарела, ананаси", "price": 300},
    {"name": "Карбонара", "ingredients": "Сливочный соус, пармезан, моцарела, бекон", "price": 290},
]

survey_results = {"Маргарита": 0, "Гавайська": 0, "Карбонара": 0}

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/menu")
def menu():
    sort_order = request.args.get("sort", "asc")
    if sort_order == "asc":
        pizzas_items = sorted(pizzas, key=lambda x: x["price"])
    elif sort_order == "desc":
        pizzas_items = sorted(pizzas, key=lambda x: x["price"], reverse=True)
    return render_template("menu.html", menu_items=pizzas_items)

@app.get("/add_pizza")
def add_pizza():
    return render_template("add_pizza.html")

@app.post("/add_pizza")
def post_add_pizza():
    form = request.form
    name = form.get("name")
    description = form.get("description")
    price = form.get("price")
    pizzas.append({
        "name": name, "description": description, "price": float(price),
    })
    return redirect(url_for("menu"))

@app.get("/survey")
def survey():
    return render_template("survey.html", pizzas=pizzas)

@app.post("/survey")
def submit_survey():
    favorite_pizza = request.form.get("favorite_pizza")
    if favorite_pizza in survey_results:
        survey_results[favorite_pizza] += 1
    return redirect(url_for("survey_results_page"))

@app.get("/survey_results")
def survey_results_page():
    return render_template("survey_results.html", results=survey_results)

if __name__ == "__main__":
    app.run(debug=True)
