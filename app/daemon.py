'''
@module: API framework
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/data-science-api-framework GitHub
@license: MIT License
@copyright: 2020 Leonardo Mauro
@access: public
'''

#-- Imports
import flask
import api
from flask import request, jsonify

#-- API predefinitions
app = flask.Flask('data-science-api')
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
appHost = 'localhost'
appPort = 5050
api.init() 


#-- Home page
@app.route('/', methods=['GET'])
def home():
    return "<h2>Data Science API Framework</h2>\
    <p>This API is running - <a href=\"http://{0}:{1}/api/\">http://{0}:{1}/api/</a>.</p>".format(appHost,appPort)


#-- API url
@app.route('/api/', methods=['GET'])
def apiRun():
    response = api.run(request.args)
    return jsonify(response)


app.run(host=appHost, port=appPort)