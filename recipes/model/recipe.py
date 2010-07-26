"""Recipe model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from recipes.model.meta import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    ingredients = Column(String)
    directions = Column(String)
    tags = Column(String)

    def __init__(self, title='', ingredients='', directions='', tags=''):
        self.title = title
        self.ingredients = ingredients
        self.directions = directions
        self.tags = tags

    def __repr__(self):
        return "<Recipe(%s)>" % self.title

