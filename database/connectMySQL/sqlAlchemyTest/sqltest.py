import sys
from os import path
sys.path.append("..")
import json
from access_token.controller import AccessTokenController
import requests
from dbHandler import CodeHubMySqlConnector
# import datetime
from datetime import timedelta, datetime

MASTER_TOKEN_URL = "https://accounts-fuse-ai-dev.auth0.com/oauth/token"
MASTER_TOKEN_GRANT_TYPE = "client_credentials"
MASTER_TOKEN_CLIENT_ID ="g57UkGrniLUSzTJYU8VYpZRtmnOlf75T"
MASTER_TOKEN_CLIENT_SECRET = "7s-4K_C-rOCHvSD5hS2JRm-QEhZ-E734e-N2wAG3eJQciss46vJrdMXfoqQou0lC"
MASTER_TOKEN_AUDIENCE = "https://fuse-ai-dev-api.fusemachines.com/"



class MissingEntry(ValueError):
    pass

def get_accesstoken():
    '''Get the access token from auth0
    :return: access token
    '''
    url = MASTER_TOKEN_URL
    data = {
        'grant_type': MASTER_TOKEN_GRANT_TYPE,
        'client_id': MASTER_TOKEN_CLIENT_ID,
        'client_secret': MASTER_TOKEN_CLIENT_SECRET,
        'audience': MASTER_TOKEN_AUDIENCE
    }
    try:
        access_token = AccessTokenController().find_access_token()
        check_token_expiry(access_token)
    except Exception:
        access_token, expires_in = request_access_token(url, data)
        AccessTokenController().add_access_token('rumancha12@gmail.com', access_token, expires_in)
    print('New mastertoken: {} '.format(access_token))
    return access_token

def check_token_expiry(token):
    print('Inside check expiry')
    print(token.modified_date)
    print(token.expires_in)
    print(datetime.now() - timedelta(seconds=token.expires_in))
    if token.modified_date > (datetime.now() - timedelta(seconds=token.expires_in)):
        print('No need to update')
    else:
        print('Need to be updated')

def get_access_token_from_db():
    return ''


def request_access_token(url: str, data: object) -> str:
    '''
    Request access token from the auth0 application
    :param url: master token auth0 url
    :param data: request json object
    :return: access token, expires time
    '''
    try:
        response = requests.post(url, data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print('Http Error : {} '.format(errh))
    except requests.exceptions.ConnectionError as errc:
        print('Error Connecting: {}'.format(errc))
    except requests.exceptions.Timeout as errt:
        print('Timeout Error: {}'.format(errt))
    except requests.exceptions.RequestException as err:
        print('OOPs: Something Else'.format(err))

    access_token = json.loads(response.text)[u'access_token']
    expires_in = json.loads(response.text)[u'expires_in']

    return access_token, expires_in


if __name__ == "__main__":
    db = CodeHubMySqlConnector().getDB()
    get_accesstoken()

