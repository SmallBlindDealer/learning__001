

import uuid
from collections import Counter
from typing import Dict
from threading import Lock

class Hotel:
    def __init__(self, name, room_catalog, total_capacity):
        self.name = name
        self.room_catalog = room_catalog  # {room_type: price}
        self.total_capacity = total_capacity
        self.remaining_capacity = total_capacity
        self.lock = Lock()
    
    def update_capacity(self, count):
        with self.lock:
            self.remaining_capacity+=count
    

class Order:
    def __init__(self, id, hotel_id, room_type,):
        ...


class HotelBookingSystem:
    def __init__(self):
        self.hotels : Dict[str, Hotel] = {}
        self.bookings: Dict[str, list[Order]] = {}
        self.lock = Lock()  # Lock to manage concurrent hotel operations

    def add_hotel(self, name, room_catalog_arr, total_capacity):
        room_catalog = {}
        for obj in room_catalog_arr:
            obj = obj.split(":")
            room_catalog[obj[0]] = float(obj[1])

        hotel = Hotel(name, room_catalog, total_capacity)
        self.hotels[str(uuid.uuid4())] = hotel

    def print_system_stats(self):
        print("Hotel name and current remaining rooms capacity")
        for hotel in self.hotels.values():
            print(f"{hotel.name}: {hotel.remaining_capacity}")
        
    def fulfilled_item_for_hotel(self, booking_id: str):
        if booking_id not in self.bookings:
            return "booking_id does not exist"
        
        # hotel_id, room_type, price, occupied_capacity
        for room in self.bookings[booking_id]:
            self.hotels[room[0]].update_capacity(room[-1])



    def book(self, room_requests, strategy="lowest_price_strategy"):
        with self.lock:
            # pre check rooms are available or not
            req_types = Counter(room_requests)

            # room_type--> hotel_id, room_type, price, remaining_capacity
            avaliable_rooms: Dict[str, list] = {}

            for id, hotel in self.hotels.items():
                for room_t in room_requests:
                    if room_t in hotel.room_catalog and hotel.remaining_capacity>0:
                        if room_t not in avaliable_rooms:
                            avaliable_rooms[room_t] = [[id, room_t, hotel.room_catalog[room_t], hotel.remaining_capacity]]
                        else:
                            avaliable_rooms[room_t].append([id, room_t, hotel.room_catalog[room_t], hotel.remaining_capacity])
            
            for room_t, req_count in req_types.items():
                if room_t not in avaliable_rooms or avaliable_rooms[room_t].__len__()<req_count:
                    return "rooms are not available for a moment"
            
            if strategy == "lowest_price_strategy" or True:
                booking_id =  self._book_lowest_price(req_types, avaliable_rooms)
                ff = ', '.join([f"{obj[-1]} {obj[1]} from '{self.hotels[obj[0]].name}'" for obj in self.bookings[booking_id]])
                print(f"Booking Id '{booking_id}' Booked {ff}")        

        

    def _book_lowest_price(self, req_types_count: Dict, avaliable_rooms: Dict[str, list]):
        booking_id = str(uuid.uuid4())
        self.bookings[booking_id] = []
        for req_t, count in req_types_count.items():
            rooms_ = sorted(avaliable_rooms[req_t], key=lambda x: x[2])
            
            c = 0
            # hotel_id, room_type, price, remaining_capacity
            for room in rooms_:
                if count==c:
                    break
                hotel_id = room[0]
                remaining_capacity = room[-1]
                if remaining_capacity<=count-c:
                    c+=remaining_capacity
                    self.bookings[booking_id].append(room)
                    self.hotels[hotel_id].update_capacity(-1*remaining_capacity)
                else:
                    room[-1] = count-c
                    self.bookings[booking_id].append(room)
                    self.hotels[hotel_id].update_capacity(-1*room[-1])
                    break


        return booking_id


a = HotelBookingSystem()
a.add_hotel("FabHotel", ["Standard Non-AC:20", "Double Deluxe:50", "Suite:60", "Sea View Suite:70"], 4)
a.add_hotel("Marriott", ["Standard AC:40", "Deluxe:30", "Double Deluxe:40", "Suite:50", "Family Suite:60", "Mountain View Suite:70"], 6)
a.add_hotel("Oyo", ["Standard Non-AC:10", "Deluxe:20"], 2)

print(a.print_system_stats())
print(a.book(["Standard Non-AC"], "lowest_price_strategy"))
print(a.print_system_stats())
print(a.book(["Standard Non-AC", "Double Deluxe"], "lowest_price_strategy"))
print(a.print_system_stats())

# print(fulfilled_item_for_hotel("#5"))
# output: Booking Id#1 : Booked from “Oyo”



