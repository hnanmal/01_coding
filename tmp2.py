# add = lambda a, b: a + b
# go = lambda ...as: reduce((a, f))

# def many_gen():
#     v = [1, 2, 3, 4]
#     yield x for x in v
#     print(list(many_gen()))


def echo(value=None):
        print("Execution starts when 'next()' is called for the first time.")
        try:
            while True:
                try:
                    value = (yield value)
                except Exception as e:
                    value = e
        finally:
            print("Don't forget to clean up when 'close()' is called.")

generator = echo(1)
print(next(generator))