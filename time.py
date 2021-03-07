import datetime
import time
for _ in range(int(input())):
    t1=input().split()
    t2=input().split()
    m1=int(time.strptime(t1[2],'%b').tm_mon)#month
    m2=int(time.strptime(t2[2],'%b').tm_mon)#month

    tim1=list(map(int,t1[4].split(":")))
    tim2=list(map(int,t2[4].split(":")))

    d1=datetime.datetime( int(t1[3]) , m1, int(t1[1]),tim1[0],tim1[1],tim1[2])
    d2=datetime.datetime( int(t2[3]) , m2, int(t2[1]),tim2[0],tim2[1],tim2[2])

    hours=int( str( t1[-1][-5:-2]     ))
    minutes=int( str( t1[-1][-2:]     ))
    d1_utc=d1+(datetime.timedelta(hours=hours,minutes=minutes))

    hours = int(str(t2[-1][-5:-2]))
    minutes = int(str(t2[-1][-2:]))
    d2_utc = d2 + (datetime.timedelta(hours=hours, minutes=minutes))

    d3=d2_utc-d1_utc

    print(d1_utc,d2_utc,d3.total_seconds(),sep="\n")









