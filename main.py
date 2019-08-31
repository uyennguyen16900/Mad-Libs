

import webapp2
import logging
import jinja2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {

        }
        template = jinja_env.get_template('templates/madlibs.html')
        self.response.write(template.render(template_vars))

class MadlibsPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'adj1': self.request.get('name'),
            'nationality': self.request.get('nationality'),
            'person': self.request.get('person'),
            'noun1': self.request.get('noun1'),
            'adj2': self.request.get('adj2'),
            'noun2': self.request.get('noun2'),
            'adj3': self.request.get('adj3'),
            'adj4': self.request.get('adj4'),
            'plural noun': self.request.get('plural_noun'),
            'noun3': self.request.get('noun3'),
            'number1': self.request.get('number1'),
            'shapes': self.request.get('shapes'),
            'food1': self.request.get('food1'),
            'food2': self.request.get('food2'),
            'verb': self.request.get('verb'),
            'number2': self.request.get('number2'),
        }
        template = jinja_env.get_template('templates/story.html')
        self.response.write(template.render(template_vars))
self.request.get(''),
