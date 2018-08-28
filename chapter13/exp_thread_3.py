#! /usr/bin/python
# -*-coding:UTF-8-*-

import threading 
from time import sleep
from datetime import datetime
  
loops = [4, 2] 
date_time_format = '%y-%M-%d %H:%M:%S'

def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)

def loop(n_loop, n_sec):
    print(f'线程（{n_loop}）开始执行:{date_time_str(datetime.now())}，先休眠（{n_sec}）秒')
    sleep(n_sec)
    print(f'线程（{n_loop}）休眠结束，结束于:{date_time_str(datetime.now())}')

def main():
    print(f'---所有线程开始执行:{date_time_str(datetime.now())}')
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in n_loops:      # start threads
        threads[i].start()

    for i in n_loops:      # wait for all
        threads[i].join()    # threads to finish

    print(f'---所有线程执行结束于:{date_time_str(datetime.now())}')

if __name__ == '__main__':
    main()
