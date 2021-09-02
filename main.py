import multiprocessing as mp

import os

from process_a import printing as pa
from process_b import printing as pb

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    print('==================')
    info('main line')
    p = mp.Process(target=f, args=('bob',))
    
    p.start()
    p = mp.Process(target=pb)
    p.start()
    p = mp.Process(target=pa)
    p.start()
    print('==================')
    p.join()