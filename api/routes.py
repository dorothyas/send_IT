from .main_views import OrderMenu

class Routes:
    @staticmethod
    def get_urls(order):
       
        orders_view = OrderMenu.as_view('parcels')
        order.add_url_rule('/api/v1/parcels', view_func=orders_view, methods=['GET'])
        order_post = OrderMenu.as_view('post_parcels')
        order.add_url_rule('/api/v1/parcels', view_func=order_post, methods=['POST'])
                        
