# scope- what variable do i have access to?

def outer():
    x = 'local'
    def inner():
        nonlocal x            # we use nonlocal here it takes x from outer function
        x = 'non local'       # here it is overriding the value of x
        print('inner:', x)

    inner()
    print('outer:', x)   # here the value of x is non local

outer()

# assigning a lot of variable or unusable variable causes problems like a lot of memory usage

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue        # here using continue will skip the banana
  print(x)
