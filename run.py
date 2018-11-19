from flask import Flask
from api.routes import Routes

APP = Flask(__name__)
Routes.get_urls(APP)

if __name__=='__main__':
    APP.run()