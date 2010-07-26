import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from recipes.lib.base import BaseController

log = logging.getLogger(__name__)

class RecipeController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/recipe.mako')
        # or, return a string
        return 'Hello World'

    def add(self):
        pass

    def delete(self):
        pass