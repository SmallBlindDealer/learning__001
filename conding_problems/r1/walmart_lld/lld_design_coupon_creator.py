
from abc import ABC
from typing import List


class User:
    def __init__(self, id):
        self.id = id
    

class Item:
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost



class Cart:
    def __init__(self):
        self.items: dict = {}
    
    def add_item(self, item: Item, qty: int):
        self.items[item] = qty
    
    def remove_item(self, item: Item, qty: int):
        ...


class Order:
    def __init__(self, id, user: User, order_value: float, cart):
        self.id = id
        self.order_value: int  = order_value
        self.user = user
        self.cart: Cart = cart
    
    def calculate_order_value(self):
        final = 0
        for item, qty in self.cart.items.items():
            final+=item.cost*qty
        
        return final

    
    def get_final_bill_summary(self):
        ...


class CouponType:
    flat = "flat"
    percentage= "percentage"


class Coupon:
    def __init__(self, coupon_type, coupon_code,exp_time, max_coupan):
        self.coupon_type: CouponType = coupon_type
        self.coupon_code: str = coupon_code
        self.exp_time = exp_time
        self.max_coupan = max_coupan
        self.itemSpecific: set = set()
        self.userSpecific: set = set()
        self.max_order_value: float = None
    
    def is_valid(self):
        ...
    
    def apply_coupon(self, order: Order):
        ...
    
    def add_items(self, item: Item):
        self.itemSpecific.add(item)
    
    def add_user(self, user: User):
        self.userSpecific.add(user)


republicDayCoupan = Coupon("percentage", "1234", None, 100)

item1 = Item(1, 5)
item2 = Item(2, 10)
item3 = Item(3, 15)


user1 = User(1)

cart_user_1 = Cart()
cart_user_1.add_item(item1, 5)
cart_user_1.add_item(item2, 10)

order_user1 = Order(1, user1)
