import os 
import queue
import threading
import time
import random

# CONSTS 
cpus = os.cpu_count()
my_q = queue.Queue()
semaphore = threading.Semaphore(3)
event = threading.Event()
starts = 10 ** 13
ends = 10 ** 20
pre_calc = 10 ** 13

def chief(s, e, p):
    bias = random.randint(s, e)
    pasta = [mass for mass in range(p, p + bias)]
    return [its_prime(mass) for mass in pasta]

def its_prime(_input):
    if _input < 2 or _input % 2 == 0:
        return False
    if _input == 2:
        return _input
    limit = int(sqrt(_input)) + 1
    for i in range(3, limit, 2):
        if _input % i == 0:
            return None
    return _input
    
class Myth(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self, callback): 
        print('initiating thread: %s' % self.name)
        callback()
        print('ending thread: %s' % self.name)



if __name__ == '__main__':
    for cpu in range(cpus):
        print(f'cpu: {cpu}, chief says: {chief(starts, ends, pre_calc)}') # meu notebook morreu depois disso, (⌐■_■)
