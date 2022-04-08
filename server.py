from flask import Flask, redirect, render_template, session, request
from random import randrange
app = Flask(__name__)
app.secret_key = "asdl;kfhjbasdl;fkhjagbsdl;fvk"

@app.route("/")
def initialize():
    # Create Random Number for User to Guess
    if "ran" not in session:
        session["ran"] = randrange(1, 100, 1)
    #If we have a guess from the form
    if "guess" in session: 
        if int(session["guess"]) > int(session["ran"]):
            return render_template("index.html", hi_lo = "Too High", reset = "hidden")
        elif int(session["guess"]) < int(session["ran"]):
            return render_template("index.html", hi_lo = "Too Low", reset = "hidden")
        else:
            return render_template("index.html", hi_lo = "You Guessed it! The number was " + str(session["ran"]) + "!", reset = "visible")
    #If we do not have a guess then initalize page
    else:
        return render_template("index.html", hi_lo = "", reset="hidden")

@app.route("/game", methods = ["post"])
def guess_game():
    session["guess"] = request.form['guess']
    return redirect("/")

@app.route("/reset", methods = ["post"])
def reset_game():
    if "reset" in request.form:
        session.clear()
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)