from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

HTML_DIR = os.path.join(os.path.dirname(__file__), "html")

@router.get("/")
async def root():
    return FileResponse(os.path.join(HTML_DIR, "index.html"), media_type="text/html")

@router.get("/git")
async def get_about_git():
    return FileResponse(os.path.join(HTML_DIR, "git.html"), media_type="text/html")

@router.get("/docker")
async def get_about_docker():
    return FileResponse(os.path.join(HTML_DIR, "docker.html"), media_type="text/html")