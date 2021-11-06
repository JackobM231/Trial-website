from flask import Flask, render_template, request

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# def apology(message, code=400):
#     """Render message as an apology to user."""
#     def escape(s):
#         """
#         Escape special characters.

#         https://github.com/jacebrowning/memegen#special-characters
#         """
#         for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
#                          ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
#             s = s.replace(old, new)
#         return s
#     return render_template("apology.html", top=code, bottom=escape(message)), code

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')
    
@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template('contact.html')

    # # User reached route via POST (as by submitting a form via POST)
    # if request.method == "POST":

    #     if not request.form.get("name") or not request.form.get("email") or not request.form.get("message"):
    #         return apology("", 400)

    # # User reached route via GET (as by clicking a link or via redirect)
    # else:
    #     return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)