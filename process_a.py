import os
def printing():
    print('this is process a')
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())