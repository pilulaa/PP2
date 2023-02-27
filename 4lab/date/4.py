import datetime 

def dif_seconds(date1, date2):
    timetilda = date2 - date1
    return timetilda.total_seconds()

date1 = datetime.datetime(2023, 2, 24, 12, 7, 34)
date2 = datetime.datetime(2023, 2, 26, 7, 34, 12)

print(dif_seconds(date1, date2))