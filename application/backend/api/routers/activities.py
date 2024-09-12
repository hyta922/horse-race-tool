import botocore
import traceback
import yaml
import service.authorization as auth
from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from logging import config, getLogger
from requests.exceptions import Timeout

router = APIRouter()

config.dictConfig(yaml.safe_load(open("logger_config.yml").read()))
logger = getLogger(__name__)

# response_model=activitys_schema.Cred
@router.post("/api/activities")
def startSession(
    activity_id: int,
    token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
):
    try:
        logger.info("Start activity")
        auth.start_activity(activity_id, token)
    except auth.ServiceError as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=400, detail=e._msg)
    except botocore.exceptions.ClientError as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Error on AWS API.")
    except auth.InvalidTokenError as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=401, detail=e._msg)
    except Timeout as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Timeout during internal process")
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Error")


@router.get("/api/activities")
def listSessions(token: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]):
    try:
        return auth.list_activities(token)
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Error")


@router.get("/api/health")
def healthCheck():
    return {"message": "Connection OK!"}
