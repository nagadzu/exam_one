# def func(list_: list) -> list:
#     list_.insert(0, 'start')
#     list_.insert(0, 'Element')
#     list_.append('finish')

#     return list_
# print(func(['hello', 5, 'John']))


# def func(*args, **kwargs) -> dict:
#     a = 0
#     dict_ = {}
#     for i in args:
#         a += 1
#     dict_.update({i: a})

#     print(dict_)

# print(func('x', 5, 'John'))


# def func(tuple_):
#     x = list(tuple_)
#     x1 = []
#     x2 = []
#     for i in x:
#         if (i % 2) == 0:
#             x1.append(i)
#         x2.append(i**2)
#     return x1,x2

# a,b = func((1,2,3,4,5))
# print(a,b)