import datetime

dt = datetime.datetime.now()
print(f"strptime is:{dt.strptime(str(dt), '%Y-%m-%d %H:%M:%S.%f')}")
