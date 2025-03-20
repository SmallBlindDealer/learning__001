

"""
10101


5-->100


file--->
log_data
find--> error name test
"""

import re
def extractTime(str_):
    return re.findall(r"^",str_)

def returnlogErroFirstLastLnNo(file_name, error_type):
    file_data = open(file_name, "r").read()
    file_data = file_name.split("/n")
    
    for obj in file_data[:]:
        if not error_type in obj:
            file_data.remove(obj)
    
    if file_data.__len__()>=2:
        return extractTime(file_data[0]), extractTime(file_data[-1])
    else:
        return extractTime(file_data[0])
            







