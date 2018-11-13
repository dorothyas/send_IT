import unittest
import json
from run import APP

class TestViews(unittest.TestCase):

    def setUp(self):
        
        self.client = APP.test_client
        self.parcel_order = dict(user_name='dorothy', user_email= 'dorothy@gmail.com',parcel_type='parcel_2',
         Weight=2, pick_up='ntinda', destination='bukoto', status='pending', user_id='3')

        self.parcel_order1 = dict(user_name='asiimwe', user_email= 'asiimwe@gmail.com',parcel_type='parcel_2',
         weight=10, pick_up='Entebbe', destination='kampala', status='pending',user_id='3')
              
    def test_can_get_all_parcels(self):
        """Method for testing the get function which returns all parcel orders"""

        self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order))
        self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order1))                            
        res = self.client().get('api/v1/parcels')
        self.assertEqual(res.status_code, 200)

    def test_can_create_parcel_order(self):
        """Method for testing the post function which posts a parcel order """

        res = self.client().post('api/v1/parcels', content_type="application/json", data=json.dumps(self.parcel_order1))
        self.assertEqual(res.status_code, 201)
       
    def test_can_get_one_order(self):
        """Method for testing the get function which returns one parcel"""

        self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order))
        self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order1))
        res = self.client().get('api/v1/parcels/2')                           
        self.assertEqual(res.status_code, 200)


    def test_cancel_parcel_order(self):
        """ Method for testing the update function """

        result1 = self.client().put('api/v1/parcels/1/cancel',
                                    content_type="application/json",
                                    data=json.dumps(dict(self.parcel_order)))
       
        self.assertEqual(result1.status_code, 200)


    def test_get_specific_user(self):
        """
            Method for testing the get function which returns one parcel_order
        """
        self.client().post('api/v1/users/1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order1))
        self.client().post('api/v1/users/a/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order))

        res = self.client().get('api/v1/users/3/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order1))
        
        self.assertEqual(res.status_code, 200)
       
               