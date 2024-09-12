import os

class EnvironmentVariables:
    def __init__(self):
        self.identity_pool_id = os.environ["IDENTITY_POOL_ID"]
        self.S3_BUCKET = os.environ["S3_BUCKET"]
        self.mode = os.environ["MODE"]

        if self.mode == "local":
            self.aws_access_key = os.environ["AWS_ACCESS_KEY"]
            self.aws_secret_key = os.environ["AWS_SECRET_KEY"]
        else:
            self.aws_access_key = None
            self.aws_secret_key = None
        
        self.rcm_url = os.environ["RCM_URL"]
        self.region_name = os.environ["REGION_NAME"]
        self.role_arn = os.environ["ROLE_ARN"]
        self.user_pool_client_id = os.environ["USER_POOL_CLIENT_ID"]
        self.user_pool_id = os.environ["USER_POOL_ID"]
