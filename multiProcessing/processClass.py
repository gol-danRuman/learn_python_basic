from multiprocessing import Process
import os

# def f(name):
#     print('hello', name)

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def g(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    q = Process(target=g, args=('bob',))
    q.start()
    q.join()
    info('main line')
    p = Process(target=g, args=('bob',))
    p.start()
    p.join()
