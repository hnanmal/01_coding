# add = lambda a, b: a + b
# go = lambda ...as: reduce((a, f))

# def many_gen():
#     v = [1, 2, 3, 4]
#     yield x for x in v
#     print(list(many_gen()))


# def echo(value=None):
#         print("Execution starts when 'next()' is called for the first time.")
#         try:
#             while True:
#                 try:
#                     value = (yield value)
#                 except Exception as e:
#                     value = e
#         finally:
#             print("Don't forget to clean up when 'close()' is called.")

# generator = echo(1)
# print(next(generator))

# a = 'my string'
# print(type(a))
# print(dir(a))

# a = 'prac'
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# # print(next(b))

class prac:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index-1
        return self.data[self.index]

a = prac('myData')

for char in a:
    print(char)
print("-"*30)


def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

a = reverse('practice')
for char in a:
    print(char)
    