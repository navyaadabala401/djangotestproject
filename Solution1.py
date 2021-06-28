from datetime import timedelta, date
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        if(date1 + timedelta(n)).weekday()==5:
            yield date1 + timedelta(n)
def getDates(date1,date2):
    date1 =str(date1)
    date2 = str(date2)
    start_dt = date(int(date1[0:4]),int(date1[4:6]),int(date1[6:8]))
    end_dt = date(int(date2[0:4]),int(date2[4:6]),int(date2[6:8]))
    for dt in daterange(start_dt, end_dt):
        year = str(dt.strftime("%Y"))
        month = str(dt.strftime("%m")) 
        first_dt = date(int(year),int(month),1)
        first_w = first_dt.isoweekday()
        if first_w == 7:
            saturday4=28
        else:
            saturday4=28-first_w
        sat_dt = date(int(year),int(month),int(saturday4))
        if dt != sat_dt:
            if dt.day%5 == 0:
                print(dt.strftime("%Y%m%d"))
        else:
            if dt.day%5 != 0:
                print(dt.strftime("%Y%m%d"))
getDates(20180728,20180927)
