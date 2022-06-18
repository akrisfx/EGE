# def per(num, base):
#     new = ''
#     while num > 0:
#         new += str(num % base)
#         num = num // base
#     return new[::-1]

# print(per(9999, 8))
# print(4**0.5 == 2)
global k
k = 4
def f (h):
    global k
    k += 1
    return k * h


print(f(2))
