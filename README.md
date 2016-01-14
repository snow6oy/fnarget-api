# api-fnarget

Fnarget exists to demonstrate the awesomeness of password-less login

## Synopsis
```
  POST / 
  person=graham  # graham does not exist
  404

  POST / 
  person=camilla # camilla accepts request
  201

  GET /camilla
  200            # you are logged in as camilla

  DELETE /camilla
  204            # logout ok
```
## Architecture
Components in the authentication flow
```
               .------.     .---------.
kodi  -------->| IPTV |-----| Web App |         
 O             .------.     .---------.   
/|\                              |
/ \            .------.     .---------.            
user  <--------|Mobile|-----|Launchkey|
               .------.     .---------.
```
Fnarget is in two parts
(1) a client called [plugin.video.fnarget], running on the IPTV software above
(2) an API shown in the Synopsis that brokers requests to Launchkey

## Test cases
The Fnarget API supports GET POST and DELETE methods 
Each method accepts a validated launchkey username
Username could be anyone of: <nobody> or graham or camilla

The following responses have been tested
```
      |nobody |graham |camilla
POST  | 400   | 401   | 201
GET   | 400   | 404   | 200 
DELETE| 400   | 404   | 204
```
### Happy path
200 "camilla is logged in"
201 Location: /camilla
204 "logout ok"

### Todo
Test Fnarget with multiple users
Create a Fnarget white label [launchkey] and register new users

## Pre-requisites
'''
 sudo python setup.py install
 Writing /usr/local/lib/python2.7/dist-packages/web.py-0.37.egg-info
'''
## Links
https://docs.launchkey.com/developer/web-desktop/sdk/python/sdk.html