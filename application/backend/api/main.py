from fastapi import FastAPI
from backend.api.routers import cognito_info
from routers import activities, metadata

app = FastAPI()
app.include_router(activities.router)
app.include_router(cognito_info.router)
app.include_router(metadata.router)