from fastapi import APIRouter, Request, Response
from fastapi.responses import RedirectResponse
from auth.msal import msal_app
from config.settings import settings

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get('/login')
async def login():
    auth_url = msal_app.get_authorization_request_url(
        scopes=['User.Read'],
        redirect_uri=settings.redirect_uri
    )
    return RedirectResponse(auth_url)

@router.get('/callback')
async def callback(request: Request, code: str):
    result = msal_app.acquire_token_by_authorization_code(
        code, scopes=['User.Read'], redirect_uri=settings.redirect_uri
    )

    if 'access_token' in result:
        response = RedirectResponse(settings.frontend_uri)
        response.set_cookie('access_token', result['access_token'])
        return response

    return {'error': 'authentication fail'}

@router.get('/me')
async def me(request: Request):
    token = request.cookies.get('access_token')

    if token:
        return {'authenticated': True}

    return Response(status_code=401)

@router.get('/logout')
async def logout():
    response = RedirectResponse(settings.frontend_uri)
    response.delete_cookie('access_token')
    return response
