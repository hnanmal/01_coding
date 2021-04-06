def number_generator():
    yield 0
    yield 1
    yield 2
    
for i in number_generator():
    print(i)
    
g = number_generator()
print(g.__next__())