import os
def printing(data):
    print('this is process b')
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    data = data + 1
    print(data)
    print('==================')
    return data 