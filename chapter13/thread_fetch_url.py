# coding=utf-8
import threading, queue, time, urllib
from urllib import request

BASE_URL = 'http://www.pythontab.com/html/pythonjichu/'
URL_QUEUE = queue.Queue()
for item in range(2, 10):
    url = BASE_URL + str(item) + '.html'
    URL_QUEUE.put(url)


def fetch_url(url_queue):
    while True:
        try:
            # 不阻塞的读取队列数据
            url_val = url_queue.get_nowait()
            url_queue.qsize()
        except Exception as ex:
            print(f'ex info is:{ex}')
            break
        curr_thread_name = threading.currentThread().name
        print(f'Current Thread Name {curr_thread_name}, Url: {url_val} ')
        try:
            response = urllib.request.urlopen(url_val)
            response_code = response.getcode()
        except Exception as ep:
            print(f'xp info is:{ep}')
            continue
        if response_code == 200:
            # 抓取内容的数据处理放这里
            # 为了突出效果， 设置延时
            time.sleep(1)


if __name__ == '__main__':
    start_time = time.time()
    threads = []
    # 可以调节线程数， 进而控制抓取速度
    thread_num = 4
    for num in range(0, thread_num):
        thread = threading.Thread(target=fetch_url, args=(URL_QUEUE,))
        threads.append(thread)
    for item_t in threads:
        item_t.start()
    for thread_t in threads:
        # 多线程多join，依次执行各线程的join方法, 确保主线程最后退出， 线程间没有阻塞
        thread_t.join()
    print(f'All thread done, spend: {(time.time() - start_time)} s')
