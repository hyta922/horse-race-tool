from fastapi import APIRouter
import backend.api.service.amplify_config_service as amplify_config_service


router = APIRouter()

@router.get("/api/cognito/amplify-config")
def amplifyConfig():
    return amplify_config_service.provideAmplifyConfig()