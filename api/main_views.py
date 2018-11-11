from flask import jsonify, request
from flask.views import MethodView


from .order_parcels import Order

order = Order()

class OrderMenu(MethodView):

    def get(self):
       
        if order.get_orders() == []:
            return jsonify ({"order":"No orders at the moment, please make order"})
        return jsonify({"orders": order.get_orders()})

    def post(self):

        data = request.get_json()

        user_name = data.get('user_name')
        parcel_type = data.get('parcel_type')
        pick_up = data.get('pick_up')
        destination = data.get('destination')
        price = data.get('price')
        status ='pending'
        parcel_id = 'parcel_id'
        
        order.create_parcel_orders(user_name, parcel_type, pick_up, destination, price, status,parcel_id)
        response_object = order.__dict__
        return jsonify(response_object) , 201


     
        

