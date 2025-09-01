from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot fut 🚀"

def keep_alive():
    t = Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))) 
    t.start()
