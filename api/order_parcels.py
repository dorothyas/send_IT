from flask import request

class Order:

    '''defines all methods'''

    def __init__(self):
        self.orders= []

    def get_orders(self):
        """method for getting all orders"""
        return self.orders
            
    def create_parcel_orders(self, user_name, user_email,parcel_type, pick_up, destination, weight, status,parcel_Id, user_id):
        """method for creating a parcel order"""
        parcels = [order for order in self.orders]
        parcel_Id = len(parcels) + 1

        order = {
            'user_name': user_name, 
            'user_email': user_email,
            'parcel_type': parcel_type,
            'pick_up': pick_up, 
            'destination': destination,
            'weight': weight,
            'status': status,
            'parcel_Id': parcel_Id,
            'user_id': user_id
        }

        self.orders.append(order)
        return self.orders

    def get_one_order(self, parcel_Id):
        """method for getting an order"""
        for order in self.orders:
            if order[parcel_Id] == parcel_Id:
                return order
            return {'Message': 'Parcel_id doesnot exist'}    
 
    
    def put(self, parcel_id):
        """method for cancelling an order"""
      
        for order in self.orders:
            if parcel_id == order['parcel_Id']:
                data = request.get_json()
                status = data['status']
                order['status'] = status
                return {'Message': 'Parcel cancelled'}
            return {'Message':'Parcel id not found'}


    def get_specific_order_by_user(self,user_id):
        """method for getting orders for a specific user"""
        
        self.users = []

        for order in self.orders:
            if user_id == order['user_id']:
                for order in self.orders:
                    if user_id == order['user_id']:
                        self.users.append(order)
                response= {
                    'User_orders': self.users
                }
                return (response)
            return ("This user has no orders yet")

    def order_exists(self, parcel_type):
        for order in self.orders:
            if parcel_type == order['parcel_type']:
                return True
            return False    