# not every iterable is a generator
# list is iterable but not a generator
# generators are usually functions
# generators uses yield
# yield pauses the function comes back to it when we do something to it, which is called next.
# it will repeatedly go to yield and ask every time for it

def generator_func(num):
    for i in range(num):
        yield i*2

# for item in generator_func(100):
#     print(item)

g = generator_func(10)
next(g)
next(g)
print(next(g))
# generator function always know the last recall
# if we exceeds the limit that we have provided in the range while calling separately using next() line by line it will throw stop iteration error.