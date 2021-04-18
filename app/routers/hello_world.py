'''
@module: API
This is how you create your your API logic
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/data-science-api-framework GitHub
@license: MIT License
@copyright: 2021 Leonardo Mauro
@access: public
'''

# Main imports
from typing import Dict, Any
from fastapi import APIRouter


# ----------------------------------------------------------------------
# Global variables
RESPONSE = {"status": "ok"}
ROUTER = APIRouter(
    prefix="/hello_world",
    tags=["hello_world"],
    responses={404: {"description": "Not found"}},
)


# ----------------------------------------------------------------------
# Endpoint router
@ROUTER.get("/")
async def health_check():
    '''
    API health check
    '''
    return RESPONSE


@ROUTER.post("/")
async def hello_world(_request: Dict[Any, Any] = None):
    '''
    API main throughput
    - request: Request entry
    '''
    return {'hello': 'world'}
