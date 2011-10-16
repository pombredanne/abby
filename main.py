#!/usr/bin/env python

from google.appengine.dist import use_library
use_library('django', '1.2')
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from oscar.models import Post

class MainHandler(webapp.RequestHandler):
    def get(self):
        Post.sync_with_path('custom/posts', keep_deleted=False, with_file_ext='html')
        posts = Post.all()
        t = template.load('custom/templates/index.html')
        c = template.Context({'items': posts})
        self.response.out.write(t.render(c))
        
#class ListHandler(webapp.RequestHandler):
#    def get(self):     
#        t = template.load('index.html')
#        posts = Post.all()
#        c = template.Context({'items': posts})
#        self.response.out.write(t.render(c))


def main():
    application = webapp.WSGIApplication([('/', MainHandler),], 
                                         debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
