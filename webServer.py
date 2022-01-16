from flask import Flask, render_template
from threading import Thread


app = Flask(__name__)


@app.route("/")
def home():
    return 'bot: .GIt#8078 is online'


def run():
    app.run(host='0.0.0.0', port=8080)
    

def wakeUp():
    t = Thread(target=run)
    t.start()