from recipes.tests import *

class TestRecipeController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='recipe', action='index'))
        # Test response...
