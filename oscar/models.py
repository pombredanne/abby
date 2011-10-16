'''
Models definitions
'''
from __future__ import with_statement
import os
#import sys
import datetime
from google.appengine.ext import db

#import logging

class Post(db.Model):
    """
    Abstract class over post provided in the `posts` directory
    @todo: handle tzinfo http://tinyurl.com/dleqec
    @todo: releted_objects realy^realy wanna have it - reviews, docs, pics + external
    @todo: load fields from html
    - title
    - subtitle
    - abstract_html
    - body_html
    - tags
    - category
    """
    title = db.StringProperty(required=True)
    subtitle = db.StringProperty()
    slug = db.StringProperty(required=True)
    abstract_html = db.StringProperty()
    body_html = db.TextProperty(verbose_name="HTML post content")
    date_created = db.DateTimeProperty(verbose_name='date created')
    date_published = db.DateTimeProperty(auto_now=True,verbose_name='date published')
    date_updated = db.DateTimeProperty(verbose_name='date updated')
#    enable_comments = db.BooleanProperty(default=False)
#    last_comment_date = db.DateTimeProperty(verbose_name='date of last comment',                                             null=True)
#    comment_count = db.IntegerProperty(default=0)
    category = db.CategoryProperty()
    tags = db.ListProperty(db.Category)
    rateing = db.RatingProperty()
    # releted_objects

    def get_absolute_url(self):
        return "/posts/%s/" % self.slug

    @classmethod
    def _get_file_meta(cls, file=None, file_path=None):
        """
        Read all the useful meta-data about the file given by `file` object or `file_path` 
        """
        if not file and file_path:
            file = open(file_path, 'r')
        file_body = file.read()
        meta = {
            'title': file.name, # read title from html
            'subtitle': 'dupa', # read from html
            'slug': os.path.splitext(os.path.basename(file.name))[0],
            'abstract_html': 'Abstract', 
            'body_html': file_body,
            'tags': [db.Category('one tag'), db.Category('second tag')],
        }
        if file_path:
            meta.update({
                'date_created': datetime.datetime.fromtimestamp(os.path.getctime(file_path)),
                'date_updated': datetime.datetime.fromtimestamp(os.path.getmtime(file_path)),
            })
        return meta

    @classmethod
    def load_from_file(cls, file=None, file_path=None):
        """
        Stores file with its metadata to DB
        """
        if not file:
            file = open(file_path, 'r')            
        if not file_path:
            file_path = file.name
        with file:
            file_meta = cls._get_file_meta(file, file_path=file_path)
            cls_properties = dict([[p, file_meta.get(p, None)] for p in cls.properties()])
            cls(key_name=file_path, **cls_properties).put()
        
    @classmethod
    def sync_with_path(cls, path, keep_deleted=True, with_file_ext=''):
        """
        Recursively read `path` and call `cls.load_from_file` for each of the files found
        
        Files that were earlier imported get replaced with newer ones.
        New ones get added. Removed files are controlled by the `keep_deleted` parameter. 
        """
        files_updated = []
        if os.path.isfile(path):
            if path.endswith(with_file_ext):
                cls.load_from_file(file_path=path)
                files_updated.append(path)
            return
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name.endswith(with_file_ext):
                    file_path = os.path.join(root, file_name)
                    cls.load_from_file(file_path=file_path)
                    files_updated.append(file_path)
        if not keep_deleted:
            to_delete = [post for post in cls.all() if post.key().id_or_name() not in files_updated]
            map(lambda p: p.delete(), to_delete)