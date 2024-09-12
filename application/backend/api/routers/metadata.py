from fastapi import APIRouter
import os

class EnvironmentVariables:
    def __init__(self):
        self.mode = os.environ["MODE"]

router = APIRouter()

@router.get("/api/metadata/mode")
def getMode():
    env_vars = EnvironmentVariables()
    return env_vars.mode
