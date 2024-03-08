from flask import Flask, render_template

from api.router import router


app = Flask(__name__)
app.register_blueprint(router)

# @app.route("/")
# def sobre():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)