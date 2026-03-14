from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from routers.auth import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_uri],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api")

api_router.include_router(auth_router)


@api_router.get("/")
def read_root():
    return {"health": "check"}

app.include_router(api_router)
