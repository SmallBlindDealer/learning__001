"""
Write a Python program to implement a URL shortener similar to Bitly.

The program should:
--> Generate a unique short URL for each input URL.
--> Allow retrieval of the original URL from the shortened version.
--> Handle collisions efficiently.
"""


import string
import random

class UrlShortener:
    
    def __init__(self):
        self.url_map = {}
        self.short_map = {}
        self.base_url = "http://abc.com/"
    

    def _generate_short_code(self, long_url):
        short_str = None
        while not short_str or short_str in self.url_map:
            short_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return short_str

    def shorten(self, long_url):
        if long_url in self.short_map:
            return self.base_url + self.short_map[long_url]
        
        short_str = self._generate_short_code(long_url)
        self.url_map[short_str] = long_url
        self.short_map[long_url] = short_str

        return self.base_url + short_str

    def retrieve(self, short_url):
        short_str = short_url.replace(self.base_url, "")
        return self.url_map.get(short_str, "URL not found")

    
# -------------------------------------------------------------------------------------------
url_shortener_obj = UrlShortener()

urls = [
    "http://sdfgfdfd.com",
    "http://dfdfddfdf.com",
    "http://fdfdvfgfg.com",
    "http://fdfdvfgfg.com",
]


for url in urls:
    tiny_url         = url_shortener_obj.shorten(url)
    actual_saved_url = url_shortener_obj.retrieve(tiny_url)

    print(url==actual_saved_url)

    print(f"tiny url: {tiny_url}\nactual_url: {url}")





# -------------------------------------------------------------------------------------------




"""
*
Follow-up questions:
*

How would you scale this solution to handle millions of URLs?
--> 
we have 2 parts:
    first:  we are receieving request to shorten url
            --> we need to save millions of urls and we have to generate shorten unique urls
            to generate shorten urls large customer on from scaling perspective we can dicouple 
            (generate_shorten_url and save_in_db) this functionally and build as a micro serivce.
            and for serving huge traffic and sudden spike we can use queueing system in between.

            why and how:
                putting both code in monolithic way will also work fine but from scaling points of 
                view we have to create replica of our service
                first challange will come-->how those replica make sure to maintain unique shorten_url
                either we can implement there caching or directly fetch from DB, or do some custom modification
                (like sharding configuration) in configuration so that whenever replica will created then 
                they will maintain uniqueness but still we have to implement to check that already exist or not.

                by decoupling this we can:
                --> eliminate custom modification logic while scaling main service 
                --> single place to change logic or maintaining shorten_url uniqueness 
                    (like by adding timestamps with shorten url to maintain uniqueness with time across there replica,
                      and reduce tech requirements around implementing to check that already exist)
                --> further scaling, we can improve. By implementing store data in chache to check unique shorten urls

                save data in DB without collisiion
                --> we can use key -value store DB Here thats help when we will have to save data in O(1) when we 
                    create multiple cluster of DB node in distributed way.
                --> for reducing to save shorten url, we can add buffer distributed cache to store and serve those 
                    urls and add batch processing logic to save multiple data in one go instedof hiting muliple time 
                    and clearing those buffer.



    second: we have to retreve actual url
            2 scieniro can be possible
            first:--> less frequest used tiny url
            sec:--> most frequest used tiny url

            major goal:
            --> reduce number of calls, directly fetching data from DB
            --> reduce caching storage

            if we will have most frequent used tiny urls above a thresold
            --> we can catch those url, either in redis cache or on server side response caching

            if we will have less frequent used tiny urls below a thresold
            --> either direct fetching from DB for low or redis cache with some timeout


What database would you use to store mappings efficiently?
    --> we can use key-value store NoSQL DB. MongoDB, Cassandra

How would you handle cache invalidation for frequently accessed URLs?
    --> redis cache with TTL

How do you guarantee uniqueness for each shortened URL:
    --> like by adding timestamps with shorten url to maintain uniqueness with time across there replica,
        and reduce tech requirements around implementing to check that already exist or not.


"""
# -------------------------------------------------------------------------------------------
