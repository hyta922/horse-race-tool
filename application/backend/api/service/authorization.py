import jwt
import json
import decimal
import yaml
import backend.api.schemas.activities as activities
from typing import List
from logging import config, getLogger
from fastapi.security import HTTPAuthorizationCredentials
from backend.api.entity.environment_variables import EnvironmentVariables

class ServiceError(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class InvalidTokenError(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg

env_vars = EnvironmentVariables()
logger = getLogger(__name__)
config.dictConfig(yaml.safe_load(open("logger_config.yml").read()))

def list_activities(
    authorize: HTTPAuthorizationCredentials,
) -> List[activities.Activities]:
    
    verify_id_token(authorize.credentials)
    response = []
    return response

def start_activity(report_id: decimal.Decimal, authorize: HTTPAuthorizationCredentials):
    verify_id_token(authorize.credentials)
    logger.info("Finish all processes")
    return json.dumps({"message": "success"})

def verify_id_token(token):
    region = env_vars.region_name
    user_pool_id = env_vars.user_pool_id
    client_id = env_vars.user_pool_client_id
    issuer = f"https://cognito-idp.{region}.amazonaws.com/{user_pool_id}"
    jwks_url = f"{issuer}/.well-known/jwks.json"
    jwks_client = jwt.PyJWKClient(jwks_url)
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    try:
        id_token = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience=client_id,
            issuer=issuer,
        )
        if id_token["token_use"] != "id":
            raise InvalidTokenError("Invalid token_use")

        return id_token
    except Exception as e:
        raise InvalidTokenError(e)
