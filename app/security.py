'''
@module: Security
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/data-science-api-framework GitHub
@license: MIT License
@copyright: 2021 Leonardo Mauro
@access: public
'''

# FastAPI
from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

# Settings
import app.config as config

# ----------------------------------------------------------------------
# Security configurations
API_KEY_HEADER = APIKeyHeader(name=config.AUTH_KEY_NAME, auto_error=False)


# ----------------------------------------------------------------------
# Auxiliar Functions
async def api_token(token: str = Security(API_KEY_HEADER)):
    '''
    API authentication token validation
    @param token: APIKeyHeader object
    '''
    if token == config.AUTH_KEY:
        return True
    raise HTTPException(status_code=403, detail="Could not validate the authentication token")
