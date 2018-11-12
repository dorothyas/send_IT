class Order:

    '''defines all methods'''

    def __init__(self):
        self.orders= []

    def get_orders(self):
        return {'All parcels': self.orders}
            
    def create_parcel_orders(self, user_name, parcel_type, pick_up, destination, weight, status,parcel_Id):
 
        parcels = [order for order in self.orders]
        parcel_Id = len(parcels) + 1

        order = {
            'user_name': user_name, 
            'parcel_type': parcel_type,
            'pick_up': pick_up, 
            'destination': destination,
            'weight': weight,
            'status': status,
            'parcel_Id': parcel_Id
        }
        self.orders.append(order)
        return self.orders

    def get_one_order(self, parcel_Id):
        parcel_id_now = [order for order in self.orders 
                               if order ['parcel_Id'] == parcel_Id]
        if not parcel_id_now:
            return {parcel_Id:"Parcel_id doesnot exist"}
        return {'Requested order': parcel_id_now}        