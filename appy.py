from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Bien venido a mi aplicación Flask!"

if __name__ == "__main__":
    app.run()
