#! /usr/bin/python
# -*-coding:UTF-8-*-

import threading 
from time import sleep
from datetime import datetime
  
loops = [4, 2]
date_time_format = '%y-%M-%d %H:%M:%S'

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)

def loop(n_loop, n_sec):
    print(f'线程（{n_loop}）开始执行:{date_time_str(datetime.now())}，先休眠（{n_sec}）秒')
    sleep(n_sec)
    print(f'线程（{n_loop}）休眠结束，结束于:{date_time_str(datetime.now())}')

def main():
    print(f'---所有线程开始执行:{date_time_str(datetime.now())}')
    threads = []
    nloops = range(len(loops))

    for i in nloops:  # create all threads
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:  # start all threads
        threads[i].start()

    for i in nloops:  # wait for completion
        threads[i].join()

    print(f'---所有线程执行结束于:{date_time_str(datetime.now())}')

if __name__ == '__main__':
    main()
