"""A simple web app made to welcome users with the use of Flask framework."""
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="template")

print("Server is running.")

@app.route("/")
def welcome():
    print("Index website opened")
    """A single welcome to the user."""
    return render_template("welcome.html")


@app.route("/hello", methods=["GET", "POST"])
def hello():
    print("Hello website opened")
    """A personalized welcome to the user."""
    if request.method == "POST":
        user_name = request.form.get("name")
        return render_template("hello_user.html", user_name=user_name)
    return render_template("hello.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
