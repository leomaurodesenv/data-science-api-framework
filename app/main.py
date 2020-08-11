'''
@module: API framework
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/data-science-api-framework GitHub
@license: MIT License
@copyright: 2020 Leonardo Mauro
@access: public
'''

#-- Imports
import config
from restplus import api
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
#-- Endpoints
from endpoints.hello_world import api as ns_hello


#-- API predefinitions
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


#-- API Configurations
def configure_app(app):
    app.config['DEBUG'] = config.FLASK_DEBUG
    app.config['ENV'] = config.FLASK_ENV
    app.config['SWAGGER_UI_DOC_EXPANSION'] = config.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    app.config['RESTPLUS_MASK_SWAGGER'] = config.RESTPLUS_MASK_SWAGGER


#-- API Init
configure_app(app)
#-- add your endpoints here
api.init_app(app)
api.add_namespace(ns_hello)


if __name__ == '__main__':
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT)
