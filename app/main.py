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
#-- Endpoints
from endpoints.hello_world import api as ns_hello


#-- API predefinitions
app = Flask(config.FLASK_NAME)


#-- API Configurations
def configure_app(app):
    app.config['DEBUG'] = config.FLASK_DEBUG
    app.config['ENV'] = config.FLASK_ENV
    app.config['RESTPLUS_VALIDATE'] = config.RESTPLUS_VALIDATE
    app.config['ERROR_404_HELP'] = config.RESTPLUS_ERROR_404_HELP
    app.config['SWAGGER_UI_DOC_EXPANSION'] = config.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    app.config['RESTPLUS_MASK_SWAGGER'] = config.RESTPLUS_MASK_SWAGGER


#-- API Init
def initialize_app(app):
    configure_app(app)
    #-- add your endpoints here
    api.init_app(app)
    api.add_namespace(ns_hello)


#-- API run
if __name__ == "__main__":
    initialize_app(app)
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT)
