import unittest
import json
from run import APP

class TestViews(unittest.TestCase):

    def setUp(self):
        
        self.client = APP.test_client
        self.parcel_order1 = dict(user_name='user_name', user_email= 'user_email',parcel_type='parcel_1',
         Price=25000, pick_up='Entebbe', destination='kampala', price=25000,status='pending')
        
         
    def test_can_get_all_parcels(self):
        """Method for tesing the get function which returns all parcel_orders"""

        res = self.client().get('api/v1/parcels')
        self.assertEqual(res.status_code, 200)

    def test_can_create_a_parcel(self):
        """Method for testing the post function which posts a parcel_order """

        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order1))
        self.assertEqual(result.status_code, 201)
       
    def test_can_get_one_order(self):
        """Method for testing method that returns one parcel"""

        result = self.client().get('api/v1/parcels/1',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order1))
        result1 = self.client().get('api/v1/parcels/x',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order1))
        self.assertEqual(result1.status_code, 404)                            
        self.assertEqual(result.status_code, 200)
               