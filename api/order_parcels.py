class Order:

    '''defines all methods'''

    def __init__(self):
        self.orders= []

    def get_orders(self):
        return self.orders
            
    def create_parcel_orders(self, user_name, parcel_type, pick_up, destination, price, status,parcel_id):
 
        parcels = [order for order in self.orders]
        parcel_id = len(parcels) + 1

        order = {
            'user_name': user_name, 
            'parcel_type': parcel_type,
            'pick_up': pick_up, 
            'destination': destination,
            'price': price,
            'status':status,
            'parcel_id': parcel_id
        }
        self.orders.append(order)
        return self.orders

    def get_one_order(self, parcel_Id):

        """ get specific order"""

        one_order = [order for order in self.orders if order['parcel_id'] == parcel_Id]
        if not one_order['parcel_id']:
            return {'parcel_id':"Parcel Id doesn't exist"}
        return {'Requested order': one_order}
