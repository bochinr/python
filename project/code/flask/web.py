from flask import Flask

app = Flask(__name__)

@app.route("/show/info")
def index():
    return "hello"

if __name__ == '__manin__':
    app.run()