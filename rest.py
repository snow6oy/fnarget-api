#!/usr/bin/python

import web
from fnarget import Fnarget

urls=('/(.*)', 'index')
fn=Fnarget()

class index:
  def POST(self, arg): # arg is silently ignored
    i = web.input()
    if not i.person:
      web.ctx.status = '400 Bad Request'
    elif fn.login(i.person):
      location = "%s://%s/%s" % (web.ctx.protocol, web.ctx.host, i.person)
      web.header('Location', location)
      web.ctx.status = '201 Created'
    else:
      web.ctx.status = '401 Not Authorized'
    return ""

  def GET(self, person):
    if not person:
      web.ctx.status = '400 Bad Request'
    if fn.whoami(person):  
      pass # default status code is 200
    else:
      web.ctx.status = '404 Not Found'
    return ""

  def DELETE(self, person):
    if not person:
      web.ctx.status = '400 Bad Request'
    elif fn.logout(person):  
      web.ctx.status = '204 No Content'
    else:
      web.ctx.status = '404 Not Found'
    return ""

if __name__ == "__main__":
  if fn.ready():
    app = web.application(urls, globals())
    app.run()
  else:
    print "not ready"