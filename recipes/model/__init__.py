"""The application's model objects"""

from sqlalchemy import orm, Column, Unicode, UnicodeText
from recipes.model.meta import Session, Base

from recipes.model.recipe import Recipe

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

orm.mapper(Recipe, recipes_table)
