# Requirements
* [Google AppEngine SDK](http://code.google.com/appengine/downloads.html)
* [Python](http://www.python.org/getit/) >= 2.5

# Usage

    git clone myblog YOURS
    cd YOURS
    externals up
Play with _custom_ and add your posts to _custom/posts_ . Then:  

    edit app.yaml
    dev_appserver.py

Each time U change something/add new posts just redeploy:
    
    appcfg.py update

# ¿Why?

* [HTML](http://www.w3.org/TR/html5/) is great markup for developers. OK, at least for some of them
* [GAE](http://code.google.com/appengine/) in mind for great environment and hosting
* [„keeping things simple”](http://en.wikipedia.org/wiki/KISS_principle) fetish got me in that case
* In one: **Simple, git versioned, free hosted blog to make love**
 
# IdeaGivers                

Great projects that keep inspiring the work on this project:
                                             
* [CouchDB](http://couchdb.apache.org/) and its [couchapps](http://couchapp.org/)
* [GitHub:pages](http://pages.github.com/)
* [toto](https://github.com/cloudhead/toto/)
* [DryDrop](http://drydrop.binaryage.com/)
* [Flask](http://flask.pocoo.org/)
* [Jekyll](https://github.com/mojombo/jekyll/)
* [gollum](https://github.com/github/gollum/) 
