

import webapp2
import logging
import jinja2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MadlibsPage(webapp2.ReuestHandler):
    def get(self):
        template_vars = {

        }
        template = jinja_env.get_template('')
