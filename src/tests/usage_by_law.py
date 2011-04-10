from db import resource 
'''
Test Code for a simple, HTML based law repository stored in github
'''

class Law(resource.Resource):
    ''' class for laws coded in html '''
    def __init__(self, path = False):
        self.history = []
        self.get(path or 'index')

    def get(self, path):
        self.marker = "src/tests/fixtures/law/%s.html" % path
        self.history.append(self.marker)

class testFreedom(UnitTest):

    def setUp(self):
        self.html = Law('freedom_of_information')

    def testHeaders(self):
        assertEqual(self.html, 'HEADER for freedom of information')


