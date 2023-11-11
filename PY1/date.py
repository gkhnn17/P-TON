#************DATATİME MODULE*****************
from datetime import datetime 
#from datetime import datetime as time
#import datetime

simdi = (datetime.now())#.today
result = simdi.year
result = datetime.ctime(simdi) #daha ayrıntılı
result =datetime.strftime(simdi,"%Y")
result =datetime.strftime(simdi,"%d %B %a")

t = '1 April 1001 hour 10:12:30'
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(dt)

birthday = datetime(1983,5,9)
print(birthday)

result = datetime.timestamp(birthday)#saniye

result = datetime.fromtimestamp(result) #saniye to datetime
result = datetime.fromtimestamp(0)

from datetime import timedelta
result = simdi + timedelta(days=10 )#days +10

print(result)
