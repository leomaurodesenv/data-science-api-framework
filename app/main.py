'''
@module: API framework
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/data-science-api-framework GitHub
@license: MIT License
@copyright: 2021 Leonardo Mauro
@access: public
'''

# FastAPI
from fastapi import FastAPI

# Security - Optional
from fastapi import Depends
from fastapi.security.api_key import APIKey
from app.security import api_token

# Settings
import app.config as config

# Routers
# include new endpoints here ---
from app.routers import hello_world


# ----------------------------------------------------------------------
# General response
RESPONSE = {"status": "ok"}

API = FastAPI(
    title=config.API_TITLE,
    description=config.API_DESCRIPTION,
    version=config.API_VERSION
)

# add new endpoints here ---
API.include_router(hello_world.ROUTER)


# ----------------------------------------------------------------------
# Main endpoints
@API.get("/")
def health_check():
    '''
    API health check
    '''
    return RESPONSE


@API.post("/securityTest")
def security(token: APIKey = Depends(api_token)):
    '''
    Test your authenticationToken
    - Configured in `security.py` file
    '''
    return RESPONSE, token
