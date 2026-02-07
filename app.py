from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🎉 Valentine est en ligne !"

if __name__ == "__main__":
    app.run()
