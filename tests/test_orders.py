import unittest
import json
from run import APP

class TestViews(unittest.TestCase):

    def setUp(self):
        
        self.client = APP.test_client

        self.parcel_order = dict(user_name='dorothy', user_email= 'dorothy@gmail.com',parcel_type='parcel_2',
         weight=2, pick_up='ntinda', destination='bukoto', user_id=3, status='pending')

        self.parcel_order1 = dict(user_name='asiimwe', user_email= 'asiimwe@gmail.com',parcel_type='parcel_2',
         weight=10, pick_up='Entebbe', destination='kampala',user_id=3, status='pending')


         
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

        res = self.client().post('api/v1/parcels', 
                                content_type="application/json", 
                                data=json.dumps(self.parcel_order1))
        self.assertEqual(res.status_code, 201)

    def test_missing_data(self):
        """Method tests missing data asserts that response status code is 400 """

        res = self.client().post('api/v1/parcels', 
                        content_type="application/json", 
                        data=json.dumps(dict(user_email= 'dorothy@gmail.com',\
                        parcel_type='parcel_2',weight=2, pick_up='ntinda', destination='bukoto',\
                            user_id=3)))
        response = json.loads(res.data.decode("utf8"))
        self.assertIn('Missing data', response['Message'])
        self.assertEqual(res.status_code, 400)


    def test_invalid_user_name(self):
        """Method tests invalid username input asserts that response status code is 400 """

        res = self.client().post('api/v1/parcels', 
                                content_type="application/json", 
                                data=json.dumps(dict(user_name='  do       ro', user_email= 'dorothy@gmail.com',\
                                parcel_type='parcel_2',weight=2, pick_up='ntinda', destination='bukoto',\
                                 user_id=3)))
        res2 = self.client().post('api/v1/parcels', 
                                content_type="application/json", 
                                data=json.dumps(dict(user_name='', user_email= 'dorothy@gmail.com',\
                                parcel_type='parcel_2',weight=2, pick_up='ntinda', destination='bukoto',\
                                user_id=3))) 
        self.assertEqual(res.status_code, 400)  
        self.assertEqual(res2.status_code, 400)                              

       


    def test_cancel_parcel_order(self):
        """ Method for testing the put function when status is not cancelled asserts status code 400 """
        
        self.client().post('api/v1/parcels',
                            content_type="application/json",
                            data=json.dumps(self.parcel_order))
        self.client().post('api/v1/parcels',
                            content_type="application/json",
                            data=json.dumps(self.parcel_order1))
        result1 = self.client().put('api/v1/parcels/1/cancel',
                                    content_type="application/json",
                                    data=json.dumps(dict(status="cancelled")))
        self.assertEqual(result1.status_code, 200)        

    
    def test_get_specific_user(self):
        """ Method for testing the get function which returns parcels orders by User """

        self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order1))
        self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(self.parcel_order))
        res = self.client().get('api/v1/users/3/parcels')
        res1 = self.client().get('api/v1/users/x/parcels')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res1.status_code, 404)
       
               