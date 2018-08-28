from atexit import register
from time import ctime
from re import compile
from threading import Thread
from urllib.request import  urlopen as uopen

REGEX = compile(b'#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp'
# AMZN = 'http://www.baidu.com'
# ISBN_DICT = {'001001': 'Python3.5 从零开始学',
#              '002002': 'Python3.7 从零开始学',
#              '003003': '人工智能'}
ISBN_DICT = {'0132269937': 'Core Python Programming',
             '0132356139': 'Python Web Development with Django',
             '0137143419': 'Python Fundamentals'}

def get_ranking(is_bn):
    page = uopen('%s%s' % (AMZN, is_bn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _show_ranking(is_bn):
    print('- %r ranked %s' % (ISBN_DICT[is_bn], get_ranking(is_bn)))

def _main():
    print('At', ctime(), 'on Amazon..')
    for is_bn in ISBN_DICT:
        Thread(target=_show_ranking, args=(is_bn,)).start()

@register
def _at_ex_it():
    print('all done at:', ctime())

if __name__ == "__main__":
    _main()