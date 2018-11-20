from flask import Flask
from api.routes.routes import Urls
from flask_jwt_extended import JWTManager


APP = Flask(__name__)
Urls.get_url(APP)
APP.config['JWT_SECRET_KEY'] = 'secretKEY' 
jwt = JWTManager(APP)

if __name__=='__main__':
    APP.run()