

import threading
import time
from collections import deque
from uuid import uuid4
import logging

logging.basicConfig(encoding='utf-8', level = logging.NOTSET)



class Customer:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Driver:
    def __init__(self, name):
        self.name = name
        self.status = 'idle'  # Can be 'idle' or 'busy'
        self.current_order = None

    def assign_order(self, order):
        self.status = 'busy'
        self.current_order = order

    def complete_order(self):
        self.status = 'idle'
        self.current_order = None

    def cancel_order(self):
        self.status = 'idle'
        self.current_order = None



# Order class to manage order details
class Order:
    def __init__(self, customer_from, customer_to, item):
        self.id = str(uuid4())
        self.customer_from: Customer = customer_from
        self.customer_to: Customer = customer_to
        self.item = item
        self.status = 'created'  # Statuses: created, assigned, picked_up(in transit), delivered, canceled
        self.driver: Driver = None
        self.created_time = time.time()

    def assign_driver(self, driver):
        self.driver = driver
        self.status = 'assigned'

    def mark_picked_up(self):
        self.status = 'in transit'

    def mark_delivered(self):
        self.status = 'delivered'

    def cancel(self):
        self.status = 'canceled'


class NotificationService:
    @staticmethod
    def notify(message):
        print(f"Notification: {message}")


class ParcelDeliverySystem:
    def __init__(self, order_place_to_assign_timeout=10, order_assign_to_pickup_timeout=10):
        # customer_name would be our primary key
        self.customers = {}
        self.drivers: dict[str, Driver] = {} 
        self.orders = {}
        self.pending_orders = deque()
        self.lock = threading.Lock()
        self.order_place_to_assign_timeout = order_place_to_assign_timeout
        self.order_assign_to_pickup_timeout = order_assign_to_pickup_timeout
    

    def onboard_customer(self, name, email, phone, address):
        with self.lock:
            if name in self.customers:
                logging.warning(f"{name} is already onboarded.")
            else:
                customer = Customer(name, email, phone, address)
                self.customers[name] = customer
                logging.info(f"Welcome {name}!")

    def onboard_driver(self, driver_name):
        with self.lock:
            if driver_name in self.drivers:
                logging.warning(f"{driver_name} is already onboarded.")
            else:
                driver = Driver(driver_name)
                self.drivers[driver_name] = driver
                logging.info(f"Welcome {driver_name}!")
                threading.Thread(target=self._assign_order, args=()).start()
    
    def driver_status(self, driver_name):
        if driver_name not in self.drivers:
            logging.warning(f"{driver_name} doesn't onboarded")
        else:
            logging.info(self.drivers[driver_name].status)
    
    def place_order(self, from_customer, item, to_customer):
        with self.lock:
            from_customer = from_customer.split(":")[1]
            to_customer = to_customer.split(":")[1]
            if from_customer not in self.customers or to_customer not in self.customers:
                logging.warning("Both customers must be onboarded.")
            else:
                order = Order(self.customers[from_customer], self.customers[to_customer], item)
                self.orders[order.id] = order
                self.pending_orders.append(order)

                logging.info(f"order is placed. Order id: {order.id}.")
                NotificationService.notify(f"to {from_customer} -> order is placed by you Order id : {order.id}")
                NotificationService.notify(f"to {to_customer} -> order is placed for you Order id : {order.id}")
                threading.Thread(target=self._assign_order, args=()).start()
                return order.id

    def _assign_order(self):
        for driver in self.drivers.values():
            if driver.status == 'idle':
                while self.pending_orders and (time.time() - self.pending_orders[0].created_time)>self.order_assign_to_pickup_timeout:
                    stale_order: Order = self.pending_orders.popleft()
                    self._monitor_order(stale_order, 0)

                if not self.pending_orders:
                    break
                curr_order: Order = self.pending_orders.popleft()
                curr_order.assign_driver(driver)
                driver.assign_order(curr_order)
                NotificationService.notify(f"to {driver.name} -> {curr_order.id} assigned to you.")
                NotificationService.notify(f"to {curr_order.customer_from.name} -> order is assigned to a driver, driver details : {driver.name}")
                NotificationService.notify(f"to {curr_order.customer_to.name} -> order is assigned to a driver, driver details : {driver.name}")
                threading.Thread(target=self._monitor_order, args=(curr_order,self.order_assign_to_pickup_timeout,)).start()


    def _monitor_order(self, order: Order, timeout=0):
        time.sleep(timeout)
        with self.lock:
            if order.status=="created" or (order.status == 'assigned' and order.driver.current_order == order):
                order.cancel()
                if order.driver:
                    order.driver.cancel_order()
                    # --searching new order for assignemnt
                    threading.Thread(target=self._assign_order, args=()).start()
                    
                NotificationService.notify(f"to {order.customer_from.name} {order.id} is canceled due to driver unavailability.")
                NotificationService.notify(f"to {order.customer_to.name} {order.id} is canceled due to driver unavailability.")
                
    def order_pickup(self, driver_name, order_id):
        with self.lock:
            if driver_name not in self.drivers or order_id not in self.orders:
                logging.warning("invalid driver or order_id")
                return
            
            driver: Driver = self.drivers[driver_name]
            order: Order = self.orders[order_id]

            if order.status=="canceled":
                logging.warning(f"order cannot be picked up. {order_id} is canceled.")
            elif order.status != 'assigned' or order.driver != driver:
                logging.warning(f"Order {order_id} cannot be picked up.")
            else:
                logging.info(f"{order_id} is picked up by the {driver_name}")
                order.mark_picked_up()
                NotificationService.notify(f"to  {order.customer_from.name}  {order.id} is picked up by the {driver_name}")
                NotificationService.notify(f"to  {order.customer_to.name}  {order.id} is picked up by the {driver_name}")


    def order_delivery(self, driver_name, order_id):
        with self.lock:
            if driver_name not in self.drivers or order_id not in self.orders:
                logging.warning("invalid driver or order_id")
                return

            driver: Driver = self.drivers[driver_name]
            order: Order = self.orders[order_id]

            if order.status in ["canceled", "delivered"]:
                logging.warning(f"Order {order_id} already {order.status}")
            elif order.status != 'in_transit':
                logging.warning(f"Order {order_id} is not in transit.")
            else:
                order.mark_delivered()
                driver.complete_order()
                NotificationService.notify(f"to  {order.customer_from.name}  {order.id} delivered by driver {driver.name}")
                NotificationService.notify(f"to  {order.customer_to.name}  {order.id} delivered by driver {driver.name}")
            
            # --searching new order for assignemnt
            threading.Thread(target=self._assign_order, args=()).start()

    def order_cancel(self, driver_name, order_id):
        with self.lock:
            if driver_name not in self.drivers or order_id not in self.orders:
                logging.warning("invalid driver or order_id")
                return

            driver: Driver = self.drivers[driver_name]
            order: Order = self.orders[order_id]

            if order.status in ["canceled", "delivered"]:
                logging.warning(f"Order {order_id} already {order.status}")
            elif order.status == 'in_transit':
                logging.warning(f"Order {order_id} is in transit, can not be cancel")
            else:
                order.cancel()
                driver.cancel_order()
                NotificationService.notify(f"to  {order.customer_from.name}  {order.id} cancelled by driver {driver.name}")
                NotificationService.notify(f"to  {order.customer_to.name}  {order.id} cancelled by driver {driver.name}")

            # --searching new order for assignemnt
            threading.Thread(target=self._assign_order, args=()).start()



    def order_status(self, order_id):
        if order_id in self.orders:
            order: Order = self.orders[order_id]
            res = f"order details -> {order_id} order is {order.status}."
            if order.status=="created":
                res+=" Waiting for driver availability."
            else:
                res+=f" Driver details: {order.driver.name}"
            logging.info(res)
        else:
            logging.warning("invalid  order_id")
   


a = ParcelDeliverySystem()
a.onboard_customer("tom", "aa@gmail.com", 123456789, "address1")
a.onboard_customer("paul", "bb@gmail.com", 987654321, "address2")
a.onboard_driver("driver1")
a.driver_status("driver1")
order_id_1 = a.place_order("from:tom", "item1", "to:paul")
a.order_pickup("driver1", order_id_1)
a.order_status(order_id_1)
order_id_2 = a.place_order("from:paul", "item2", "to:tom")
a.order_status(order_id_2)
time.sleep(a.order_assign_to_pickup_timeout)
a.onboard_driver("driver2")
a.order_pickup("driver2", order_id_2)





