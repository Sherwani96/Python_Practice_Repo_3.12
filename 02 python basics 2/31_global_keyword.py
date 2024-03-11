# parameters pass to the function are local variables or of local scope.

# scope of a variable
total = 0

# if we want to update the value of total variable declared in global scope so we need to use global keyword
def count():
    global total
    total += 1
    return total

count()
count()
print(count())

# ______ but the above code or function is not the good practice if you're going to work on large projects or it might be difficult__________________

total = 0
def count(total):   # here in order to access the global variable we need to pass it as a parameter
    total += 1
    return total

print(count(count(count(total))))
