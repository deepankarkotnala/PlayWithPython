# Decorators in Python

A **decorator** is a function that takes a function as its only parameter and returns a function. This is helpful to “wrap” functionality with the same code over and over again. 

```python
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
```
