def MostFreeTime(strArr):

  arr = []

  def convert_in_unix(str_time):
    cur = 0
    hr, m = str_time[:-2].split(":")
    cur+=(int(hr)*60 + int(m))

    if "PM" in str_time:
      if int(hr) not in [12]:
        cur+=12*60
    return cur

  for obj in strArr:
    start, end = obj.split("-")
    arr.append([convert_in_unix(start), convert_in_unix(end)])
  
  arr.sort()

  max_time = 0
  for idx in range(1, len(arr)):
    if arr[idx][0]-arr[idx-1][-1]>max_time:
      max_time = arr[idx][0]-arr[idx-1][-1]
  
  hr = max_time//60
  mi = max_time%60
  return (str(hr) if hr>=10 else ("0"+str(hr))) + ":" +(str(mi) if mi>=10 else ("0"+str(mi)))

for obj in [["07:00AM-08:00AM","09:00AM-10:00AM","10:00PM-11:00PM"]]:
  print(MostFreeTime(obj))