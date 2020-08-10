#-- Imports
import config
from flask_restplus import Api


#-- API global var
api = Api(version=config.RESTPLUS_VERSION, title=config.RESTPLUS_TITLE,
    description=config.RESTPLUS_DESCRIPTION,
)


#-- 500
# @api.errorhandler
# def default_error_handler(e):
#     message = 'An unhandled exception occurred.'
#     return {'message': message}, 500