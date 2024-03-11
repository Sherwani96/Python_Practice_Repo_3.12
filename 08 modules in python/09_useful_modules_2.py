import datetime, time, array

print(datetime.time(2,3,4)) # it takes time in hr:min:sec format
print(datetime.date.today()) # it prints today's date
# we use date time module if we have a timer for something to check

print(time.time()) # it prints time is ms

# lists in python are dynamic
# array which python gives us consumes less memory and are faster

li = array.array('i', [1,2,3])  # here i is the allocation of memory size to each item in list
print(li[1])