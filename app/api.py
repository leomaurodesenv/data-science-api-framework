'''
@module: API
This is where you will place your API logic
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/data-science-api-framework GitHub
@license: MIT License
@copyright: 2020 Leonardo Mauro
@access: public
'''

# Called when the service is loaded
def init():
    '''
    Init webservice
    - Usually used to initialize the main variables
    @access: private
    '''
    global varExample
    varExample = 'This is a var from init()'


# Called when the API is requested
def run(args):
    '''
    API logic
    @param args: GET parameters (dict)
    @return: API response (dict)
    @access: private
    '''
    global varExample
    response = args.copy()
    response['message'] = varExample
    return response