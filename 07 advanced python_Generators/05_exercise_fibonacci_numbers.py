# fibonacci sequence follows ((n-1) + n), the last is summed to the present sequenced to form a new or succeeding sequence

# fibonacci sequence numbers generator function
def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(5):
    print(x)

