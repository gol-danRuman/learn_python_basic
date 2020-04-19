

from sqlalchemy.orm.exc import NoResultFound

from .models import AccessToken
import logging
import datetime

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

class MissingEntry(ValueError):
    pass

from db import Session, MissingEntry

session = Session()

from db import Base, new_uuid

class AccessTokenController():

    ## add new or update existing assignment in the database
    @classmethod
    def add_access_token(self, access_token, expires_in):
        '''

        :param email: user email id
        :param access_token: master access token
        :param expires_in: time expires in
        :param created_date: token created date time
        :param modified_date: token modified date time
        :return: access token object
        '''
        try:
            access_token = self.find_access_token()
            access_token = AccessToken(
                id=access_token.id,
                access_token=access_token,
                expires_in=expires_in,
                created_date=access_token.created_date,
                modified_date=datetime.datetime.utcnow()
            )
            logger.info('Access Token updated : {}'.format(access_token.to_dict()))
        except Exception:
            access_token = AccessToken(
                id=new_uuid(),
                access_token=access_token,
                expires_in=expires_in,
                created_date=datetime.datetime.utcnow(),
                modified_date=datetime.datetime.utcnow(),
            )
            logger.info('Access Token added : {}'.format(access_token.to_dict()))
        session.add(access_token)
        session.commit()
        return access_token

    ## find the assignment using assignment name
    @classmethod
    def find_access_token(self):
        '''
        Get access token for email id
        :param email: current user email id
        :return:  access token object
        '''
        try:
            access_token = session.query(AccessToken).first()
        except NoResultFound:
            raise Exception('No such access_token found: {}'.format(email))
        return access_token
