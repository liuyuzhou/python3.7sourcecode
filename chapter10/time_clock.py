import time

def procedure():
    time.sleep(2)

# measure process time
t1 = time.clock()
procedure()
print(f'seconds process time : {(time.clock() - t1)}')

# measure wall time
t2 = time.time()
procedure()
print(f'seconds wall time : {(time.time() - t2)}')
