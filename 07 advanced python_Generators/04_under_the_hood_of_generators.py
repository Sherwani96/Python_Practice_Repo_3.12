class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0,100)
# for i in gen:
#     print(i)

gen.__next__()
print(gen.__next__())

gen.__iter__()
print(gen.__iter__())
