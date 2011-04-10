from db import resource 
'''
Test Code for a simple, HTML based law repository stored in github
'''

class Act(resource.Resource):
    ''' class for laws coded in html '''
    def __init__(self, path = False):
        self.history = []
        self.get(path or 'index')

    def get(self, path):
        self.marker = "src/tests/fixtures/law/%s" % path
        self.history.append(self.marker)

class testFreedom(UnitTest):

    def setUp(self):
        self.html = Act('freedom_of_information')

    def testHeaders(self):
        assertEquals(self.html.readline(), 'FIRST LINE of freedom of information Act')
        assertEquals(self.html.readline(), 'SECOND LINE')
        assertEquals(self.html.readline(), 'THIRD LINE')


