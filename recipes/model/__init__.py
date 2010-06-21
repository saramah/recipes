"""The application's model objects"""

from sqlalchemy import orm, Column, Unicode, UnicodeText
from recipes.model.meta import Session, Base


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

class Recipe(Base):
    __tablename__ = 'recipes'
    title = Column(Unicode(40), primary_key=True)
    ingredients = Column(UnicodeText(), default=u'')
    directions = Column(UnicodeText(), default=u'')
    tags = Column(UnicodeText(), default=u'')

class Recipe(object):
    
    def __init__(self, title, ingredients=None, directions=None, tags=None):
        self.title = title
        self.ingredients = ingredients
        self.directions = directions
        self.tags = tags

    def __unicode__(self):
        return self.title

   __str__ = __unicode__

orm.mapper(Recipe, recipes_table)
