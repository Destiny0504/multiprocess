import os
def printing(data):
    print('this is process a')
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    data = data + 1
    print('==================')
    return data 