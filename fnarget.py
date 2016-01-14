#!/usr/bin/python
import launchkey, time, logging, sys

class Fnarget:
  person=None
  authReqToken=None
  api=None
  logging.basicConfig(stream=sys.stdout, level=logging.INFO)

  # load the API credentials for launchkey
  def __init__(self):
    pvtKey=open('private.key', "r").read()
    creds={}
    with open('api.key', 'r') as f:
      for line in f:
        key, val=line.partition("=")[::2]
        creds[key]=str(val.strip())
    api=launchkey.API(creds['rocket'], creds['secret'], pvtKey)
    Fnarget.api=api

  def login(self, person):
    """login [person] Start a session for the named person
    <person> is a LaunchKey username, user hash, or white label client app identifier"""
    session=True
    userPushId=False
    numOfRetries=10 # give person 30s to respond (can be up to 5m)
    timeOut=True
    if Fnarget.person:
      logging.debug(Fnarget.person+ " is already logged in")
    elif person:
      authReqToken=self.api.authorize(person, session, userPushId)
      logging.debug("authReqToken:"+ authReqToken)
      # example authResponse
      """ {'successful': False, 
           'status_code': 400, 
           'message': 'Pending response', 
           'message_code': 70403, 
           'response': ''}"""
      for i in range(1, numOfRetries+1):
        # Validate an auth Request returned from the authorize call
        authResponse=self.api.poll_request(authReqToken)
        # the 'successful' attribute of the response contains the status
        if 'successful' in authResponse and not authResponse['successful']:
          logging.debug("login status is '%s'" % (authResponse['message']))
          logging.debug("retrying (%d of %d)" % (i, numOfRetries))
          time.sleep(5.0)
        if 'auth' in authResponse:
          timeOut=False
          break
      if timeOut:
        logging.debug("no response to login request")
      elif self.api.is_authorized(authReqToken, authResponse['auth']):
        Fnarget.person=person
        Fnarget.authReqToken=authReqToken
        logging.debug("session started for "+ Fnarget.person)
        return True
      else:
        logging.debug(person+ " declined to accept the login request")
    else:
      logging.debug("need to know who you are before i can log you in")
    return False

  def whoami(self, person):
    """Check to see if a local session exists already"""
    if Fnarget.person:
      logging.debug("you are logged in as "+ Fnarget.person)
      return True
    else:
      logging.debug("nobody is logged in")
      return False

  def logout(self, person):
    """Close or de-orbit the given session"""
    if Fnarget.person and self.api.logout(Fnarget.authReqToken):
      Fnarget.person=None
      logging.debug("logout ok")
      return True
    else:
      logging.debug("nobody was logged in or API returned an error")
      return False

  # check access to API is available
  def ready(self):
    if self.api:
      api_ping=self.api.ping()
      logging.debug("launchkey_time %s" % api_ping['launchkey_time'])
      if api_ping['launchkey_time']:
        return True
      else:
        return False
