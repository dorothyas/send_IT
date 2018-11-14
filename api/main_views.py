from flask import jsonify, request
from flask.views import MethodView
import re


from .order_parcels import Order

order = Order()


class OrderMenu(MethodView):


    def post(self):
       

        keys = ("user_name","parcel_type", "pick_up","destination","weight","user_email", "user_id")
        data = request.get_json()
        if not set(keys).issubset(set(request.json)):
            return jsonify({"message":'missing in data'}), 400

        if data['user_name'] == "":
            return jsonify({'Message':'Enter Username'}), 400

        if ' ' in data['user_name']:
            return jsonify({'Message':'User name should not contain any spaces'}), 400

        if data['parcel_type'] == "":
            return jsonify({'Message':'Enter Parcel Type'}), 400

        if ' ' in data['parcel_type']:
            return jsonify({'parcel':'Parcel type should not contain any spaces'}), 400

        if not isinstance(data['weight'], int):
            return jsonify({'weight':'Weight should be an integer'}), 400

        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, data['user_email']):
            return jsonify({'message':'Enter valid Email'}), 400

        user_name = data['user_name']
        user_email = data['user_email']
        parcel_type = data['parcel_type']
        pick_up = data['pick_up']
        destination = data['destination']
        weight = data['weight']
        status ='pending'
        parcel_id = 'parcel_id'
        user_id = data['user_id'] 

        order.create_parcel_orders(user_name, user_email, parcel_type, pick_up, destination, weight, status, parcel_id, user_id)
        response_object = order.__dict__
        return jsonify(response_object) , 201

    def get(self, parcel_Id=None, user_id= None):
        if user_id is None:    
            if parcel_Id is None:
                if order.get_orders() == []:
                    return jsonify ({"order":"No orders"}),404
                return jsonify(order.get_orders()),200
            return jsonify (order.get_one_order(parcel_Id)), 200
        return jsonify(order.get_specific_order_by_user(user_id))

    def put(self, parcel_Id):
        return jsonify({'parcel_id': order.put(parcel_Id)})



    

     
        

