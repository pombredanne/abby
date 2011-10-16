#!/usr/bin/env python


import webapp2 as webapp

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('OK')
#        Post.sync_with_path('custom/posts', keep_deleted=False, with_file_ext='html')
#        posts = Post.all()
#        t = template.load('custom/templates/index.html')
#        c = template.Context({'items': posts})
#        self.response.out.write(t.render(c))
        
#class ListHandler(webapp.RequestHandler):
#    def get(self):     
#        t = template.load('index.html')
#        posts = Post.all()
#        c = template.Context({'items': posts})
#        self.response.out.write(t.render(c))


application = webapp.WSGIApplication([
    ('/', MainHandler),
],debug=True)

def main():
    webapp.util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
