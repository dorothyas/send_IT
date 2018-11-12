from flask import jsonify, request
from flask.views import MethodView


from .order_parcels import Order

order = Order()

class OrderMenu(MethodView):

    def get(self, parcel_Id):
        if parcel_Id is None:
            if order.get_orders() == []:
                return jsonify ({"order":"No orders"}),404
            return jsonify(order.get_orders()),200
        return jsonify (order.get_one_order(parcel_Id)), 200

    def post(self):

        data = request.get_json()

        user_name = data.get('user_name')
        parcel_type = data.get('parcel_type')
        pick_up = data.get('pick_up')
        destination = data.get('destination')
        weight = data.get('weight')
        status ='pending'
        parcel_id = 'parcel_id'
        
        order.create_parcel_orders(user_name, parcel_type, pick_up, destination, weight, status, parcel_id)
        response_object = order.__dict__
        return jsonify(response_object) , 201

    

     
        

