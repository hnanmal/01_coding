# def map(f, list):
#     for a in list:
#         yield f(a)

# def f(list, length):
#     i = 0
#     acc = 0
#     for a in map(a**2, filter(a%2, list)):
#         acc = acc + a
#         if ++i == length:
#             break


# def main():
#     f([1,2,3,4,5], 3)

# print(main())

# my_gen = (x for x in range(1, 11) if x % 2 == 0)
# print(list(my_gen))


# def generate_mk(N):
#    for i in range(N):
#        yield i

# gen = generate_mk(3)
# next(gen)
# next(gen)
# next(gen)

# def counter(maximum):
#     i = 0
#     while i < maximum:
#         val = (yield i)
#         # If value provided, change counter
#         if val is not None:
#             i = val
#         else:
#             i += 1


# def is_even(x):
#     return (x % 2) == 0

# print(
#     list(
#         filter(
#             is_even, 
#             range(10)))
#     )