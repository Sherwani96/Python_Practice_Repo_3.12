from time import time
# decorator


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'This Took {t2 - t1} ms.')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000):
        i*5

long_time()

# decorators use cases
# used in python libraries and frameworks
# frameworks like django and flask use decorators
# use as authentication decorator
# logging system information
