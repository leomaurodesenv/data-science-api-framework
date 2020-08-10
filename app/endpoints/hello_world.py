'''
@module: API
This is where you will place your API logic
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/data-science-api-framework GitHub
@license: MIT License
@copyright: 2020 Leonardo Mauro
@access: public
'''

#-- Imports
from flask_restplus import Namespace, Resource


#-- Endpoint
api = Namespace('hello', description='Hello World endpoint')


#-- API logic
@api.route('/')
class HelloWorld(Resource):
    # Called when the API is requested
    @api.doc('get_hello')
    def get(self):
        '''
        Hello World
        @return: API response (dict)
        @access: public
        '''
        return {'hello': 'world'}


@api.route('/<value>')
@api.param('value', 'GET value')
class HelloWorldSend(Resource):
    # Called when the API is requested
    @api.doc('send_value_hello')
    def get(self, value):
        '''
        GET value example
        @param args: GET parameters (dict)
        @return: API response (dict)
        @access: public
        '''
        return {'get': value}
