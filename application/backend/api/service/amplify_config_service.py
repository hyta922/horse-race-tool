from jinja2 import Environment, FileSystemLoader
import os
import json

def provideAmplifyConfig():
    env = Environment(loader=FileSystemLoader(os.path.dirname(__file__), encoding='utf8'))
    params = {
        'region': os.environ['REGION_NAME'],
        'user_pool_id' : os.environ['USER_POOL_ID'],
        'user_pool_client_id': os.environ['USER_POOL_CLIENT_ID'],
        'cognito_endpoint_url' : os.environ['COGNITO_ENDPOINT_URL'].replace('https://', '')
    }
    tmpl = env.get_template('amplifyConfig.json.j2')
    data = json.loads(tmpl.render(params))

    return data
