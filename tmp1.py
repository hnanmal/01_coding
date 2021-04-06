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

my_gen = (x for x in range(1, 11) if x % 2 == 0)
print(list(my_gen))