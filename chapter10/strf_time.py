import time

t = (2018, 3, 11, 16, 50, 38, 6, 48, 0)
t = time.mktime(t)
print(time.strftime('%b %d %Y %H:%M:%S', time.gmtime(t)))
