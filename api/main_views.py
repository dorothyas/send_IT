from flask import jsonify, request
from flask.views import MethodView
import re


from .order_parcels import Order

order = Order()


class OrderMenu(MethodView):


    def post(self):

        keys = ("user_name","parcel_type", "pick_up","destination","weight","user_email")
       
        if not set(keys).issubset(set(request.json)):
            return jsonify({'Message': 'fill in all the required fields'}), 400

        if request.get_json('user_name') == "":
            return jsonify({'Message':'Enter Username'}), 400

        if (' ' in request.get_json('user_name')) == True:
            return jsonify({'Message':'User name should not contain any spaces'}), 400

        if request.get_json('parcel_type') == "":
            return jsonify({'Message':'Enter Parcel Type'}), 400

        if (' ' in request.get_json('parcel_type')) == True:
            return jsonify({'parcel':'Parcel type should not contain any spaces'}), 400

        # if not isinstance(request.get_json('weight'), int):
        #     return jsonify({'weight':'Weight should be an integer'}), 400

        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, request.json['user_email']):
            return jsonify({'message':'Enter valid Email'}), 400

        data = request.get_json()
        user_name = data.get('user_name')
        user_email = data.get('user_email')
        parcel_type = data.get('parcel_type')
        pick_up = data.get('pick_up')
        destination = data.get('destination')
        weight = data.get('weight')
        status ='pending'
        parcel_id = 'parcel_id'
        order.create_parcel_orders(user_name, user_email, parcel_type, pick_up, destination, weight, status, parcel_id)
        response_object = order.__dict__
        return jsonify(response_object) , 201

    def get(self, parcel_Id):

        if parcel_Id is None:
            if order.get_orders() == []:
                return jsonify ({"order":"No orders"}),404
            return jsonify(order.get_orders()),200
        return jsonify (order.get_one_order(parcel_Id)), 200

    def put(self, parcel_Id):
        return jsonify({'parcel_id': order.put(parcel_Id)})



    

     
        

