from flask import Flask

from threading import Thread
import os

app = Flask('')

@app.route('/')

def home():
  return "Webserver OK,Discord Bot OK"
          

def run():
  print('ta vivo')
  app.run(host="0.0.0.0",port= os.environ.get('PORT'))


def keep_alive():
  t = Thread(target=run)
  t.start()