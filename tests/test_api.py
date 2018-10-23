''' Test API '''
import api

import falcon
from falcon import testing


class MyTestCase(testing.TestCase):
    ''' Setup test of my api '''

    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = api.create()


class TestApi(MyTestCase):
    ''' Test Comic Creators' names Twitter search '''

    def test_get_t_king(self):
        ''' Test Tom King query '''
        query = {'creator': 'Tom King'}
        result = self.simulate_get('/', params=query)
        self.assertEqual(result.status, falcon.HTTP_200)

    def test_get_s_snyder(self):
        ''' Test Scott Snyder query '''
        query = {'creator': 'Scott Snyder'}
        result = self.simulate_get('/', params=query)
        self.assertEqual(result.status, falcon.HTTP_200)

    def test_get_j_jones(self):
        ''' Test Joelle Jones query '''
        query = {'creator': 'Joelle Jones'}
        result = self.simulate_get('/', params=query)
        self.assertEqual(result.status, falcon.HTTP_200)

    def test_get_j_tynion(self):
        ''' Test James Tynion query '''
        query = {'creator': 'James Tynion'}
        result = self.simulate_get('/', params=query)
        self.assertEqual(result.status, '200 OK')

    def test_get_g_johns(self):
        ''' Test Geoff Johns query '''
        query = {'creator': 'Geoff Johns'}
        result = self.simulate_get('/', params=query)
        self.assertEqual(result.status, falcon.HTTP_200)

    def test_get_j_robinson(self):
        ''' Test James Robinson query '''
        query = {'creator': 'James Robinson'}
        result = self.simulate_get('/', params=query)
        self.assertEqual(result.status, falcon.HTTP_200)
    
    def test_no_creator_parameter(self):
        ''' Test if creator parameter is not present  '''
        result = self.simulate_get('/')
        self.assertEqual(result.status, falcon.HTTP_404)
    
    def test_unsupported_creator_parameter(self):
        ''' Test if creator parameter is unsupported  '''
        query = {'creator': 'John Smith'}
        result = self.simulate_get('/', params=query)
        self.assertEqual(result.status, falcon.HTTP_406)

    def test_unsupported_parameter(self):
        ''' Test if given parameter is unsupported  '''
        query = {'name': 'John Smith'}
        result = self.simulate_get('/', params=query)
        self.assertEqual(result.status, falcon.HTTP_404)
