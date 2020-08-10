# Flask settings
FLASK_NAME = 'ds-api'
FLASK_HOST = '0.0.0.0'
FLASK_PORT = '5050'
FLASK_ENV = 'production'
FLASK_DEBUG = False  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_VERSION = '0.3.3'
RESTPLUS_TITLE = 'Data Science API'
RESTPLUS_DESCRIPTION = 'A simple framework to test and deploy your Data Science API.'
RESTPLUS_VALIDATE = True
RESTPLUS_ERROR_404_HELP = False
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_MASK_SWAGGER = False
