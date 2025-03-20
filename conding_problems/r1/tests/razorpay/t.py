"""
cron sp
*/15    0   1,15    *   1-5     /usr/bin/find

0/15    1   1,15    *   1-5     /usr/bin/find

minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find


0/15    -  0 15 30 45
0 	    -  0
1,15    -  1 15
*     	   1 2 3 4 5 6 7 8 9 10 11 12
1-5		-  1 2 3 4 5



INPUT:

minute	hour day of month		month		day of week		command

0/15 	2,3 	1,15 				* 			1-5 			/usr/bin/find

---------------_---------------_---------------_---------------_---------------_---------------_


OUTPUT:

minute        0 15 30 45 60
hour          2 3
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find



15 	2/3 	1-6 				1 			1,5 			/usr/bin/find

---------------_---------------_---------------_---------------_------------
15 	2/3 	1-6 				1 			1,5 			/usr/bin/find

---------------_---------------_---------------_---------------_---------------_---------------_

- --> continues
, --> mentioned value only after split
/ --> start pre on post interval
else--> metioned value

OUTPUT:

minute        15
hour          2 5 8 11 14 17 20 23
day of month  1 2 3 4 5 6
month         1
day of week   1 5
command       /usr/bin/find
"""


import enum

class DataType(enum.Enum):
    minute = 1
    hour = 2
    day_of_month = 3
    month = 4
    day_of_week = 5


class TimeObj:
    def __init__(self, type, max_interval):
        self.type = type
        self.min_interval = 0
        self.max_interval = max_interval
        self.interval_list = []
    
class Response:
    def __init__(self):
        self.minute = TimeObj(DataType.minute, 60)
        self.hour = TimeObj(DataType.hour, 24)
        self.day_of_month = TimeObj(DataType.day_of_month, 31)
        self.month = TimeObj(DataType.month, 12)
        self.day_of_week = TimeObj(DataType.day_of_week, 7)
        self.command = None
    

class CronSpecialProcessor:

    def __init__(self):
        self.mappings = {
            0: DataType.minute,
            1: DataType.hour,
            2: DataType.day_of_month,
            3: DataType.month,
            4: DataType.day_of_week
        }


    def process_string(input_string):
        input_string = input_string.split(" ")
        if len(input_string)!=6:
            raise Exception("not proper string")
        
        res = Response()
    

    def return_arr_of_freq(input_string, timeObj: TimeObj=None):
        """
        - --> continues
        , --> mentioned value only after split
        / --> start pre on post interval
        else--> metioned value
        """

        if not timeObj:
            return [input_string]
        
        import abc
        class ExcutionLogic(abc.ABC):
            def return_arr_of_freq(str_arr):
                ...
        
        class Dash(ExcutionLogic):
            def _init__(self):
                self.type = "-"
            
            def return_arr_of_freq(str_arr):
                ...

        for char in ["-", "/", ","]:
            if char in input_string:
                ...
                break

        # if "-" in input_string and len(input_string.split("-"))==2:
        #     input_string = [int(i) for i in input_string.split("-")]
        #     if input_string[1]>timeObj.max_interval or input_string[0]<timeObj.min_interval:
        #         ...
        #     return [i for i in range(int(input_string[0], int(input_string[1]+1)))]
        
        # elif "," in input_string and len(input_string.split(","))==2:
        #     input_string = input_string.split(",")
        #     return [input_string[0], input_string[1]]
        
        # elif "/" in input_string and len(input_string.split("/"))==2:
        #     input_string = input_string.split("/")
        #     pre = input_string[0]
        #     if pre=="*":
        #         pre = 0
        #     else:
        #         pre = int(pre)
        #     post = int(input_string[1])
        #     ll = []
        #     for i in range(pre, timeObj.max_interval+1, post):
        #         ll.append(i)
            
        #     return ll



a = CronSpecialProcessor()
a.process_string('*/15 0 1,15 * 1-5 /usr/bin/find')



"""

OUTPUT:

minute        15
hour          2 5 8 11 14 17 20 23
day of month  1 2 3 4 5 6
month         1
day of week   1 5
command       /usr/bin/find


how to define schema



CronTask:
    task_id -->index
    encoded_string
    start_from_datetime
    curr_call_time
    next_cal_time --> index
    is_active  --> index
    cmd


TaskExecutionInfo:
    task_id   -->forignkey
    status    --> success/failure
    create_at --> 




how to call API for cron

POST: /register_task
body: {
    "encoded_string": '*/15 0 1,15 * 1-5 /usr/bin/find',
    "start_from_datetime": None
}

Put: /stop_task/<task_id>

Delete: /delete_task/<task_id>


Get: /task_info/<task_id>?order_by=ASE

select * from TaskExecutionInfo

response: 
[
    {created_at: "", status: ""},
    {created_at: "", status: ""},
]









"""