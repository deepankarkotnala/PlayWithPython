import math
import time

def calculate_time(func):

    def inner_fn(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        print("Time taken to execute \'{}\' function is: {} seconds".format(func.__name__, round(end - start, 2)))
        
    return inner_fn

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(20)