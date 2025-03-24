"""
photo.jpg, Warsaw, 2013-09-05 14:08:15 
john.png, London, 2015-06-20 15:13:22 
myFriends.png, Warsaw, 2013-09-05 14:07:13 
Eiffel.jpg, Paris, 2015-07-23 08:03:02 
pisatower.jpg, Paris, 2015-07-22 23:59:59 
BOB.jpg, London, 2015-08-05 00:02:03 
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2015-09-01 15:40:22 
a.png, Warsaw, 2016-02-13 13:33:50 
b.jpg, Warsaw, 2016-01-02 15:12:22 
c.jpg, Warsaw, 2016-01-02 14:34:30 
d.jpg, Warsaw, 2016-01-02 15:15:01 
e.png, Warsaw, 2016-01-02 09:49:09 
f.png, Warsaw, 2016-01-02 10:55:32 
g.jpg, Warsaw, 2016-02-29 22:13:11

your function should return: 
Warsaw02.jpg 
London1.png 
Warsaw01.png 
Paris2.jpg 
Paris1.jpg 
London2.jpg 
Paris3.png 
Warsaw03.jpg 
Warsaw09.png 
Warsaw07.jpg 
Warsaw06.jpg 
Warsaw08.jpg 
Warsaw04.png 
Warsaw05.png 
Warsaw10.jpg 



"""
text = """photo.jpg, Warsaw, 2013-09-05 14:08:15 
john.png, London, 2015-06-20 15:13:22 
myFriends.png, Warsaw, 2013-09-05 14:07:13 
Eiffel.jpg, Paris, 2015-07-23 08:03:02 
pisatower.jpg, Paris, 2015-07-22 23:59:59 
BOB.jpg, London, 2015-08-05 00:02:03 
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2015-09-01 15:40:22 
a.png, Warsaw, 2016-02-13 13:33:50 
b.jpg, Warsaw, 2016-01-02 15:12:22 
c.jpg, Warsaw, 2016-01-02 14:34:30 
d.jpg, Warsaw, 2016-01-02 15:15:01 
e.png, Warsaw, 2016-01-02 09:49:09 
f.png, Warsaw, 2016-01-02 10:55:32 
g.jpg, Warsaw, 2016-02-29 22:13:11""".split("\n")

class CityImages:
    def __init__(self, name):
        self.name = name
        self.images = []
        self.sorted_renamed_data = []
    
    def sort_and_rank(self):
        ...


class ReformatIngestionImage:
    ...
    def __init__(self):
        self._city = {"": CityImages()}
    
    def ingest_data(text):
        ...

    def retun_final(self):
        ...
    
    def rename_format(self, input):
        ...
    

from datetime import datetime

def solution(text_):
    temp = []
    for idx, sen in enumerate(text_):
        sen = sen.split(", ")
        temp.append([sen[1], sen[2], idx])
    
    for city in set([i[0] for i in temp]):
        data = list(filter(lambda x: x[0]==city, temp))
        sorted_data = sorted(data, key=lambda x: x[1])
        for idx, obj in enumerate(sorted_data):
            text[obj[-1]] = obj[0]+str(idx+1)
    print(text_)


solution(text)
    

