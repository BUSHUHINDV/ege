# def direct_translation(n, base):
#     result = ''
#     if base == 16:
#         while n > 0:
#             r = n % 10000
#             if r == 0:
#                 result = str(0) + result
#             if r == 1:
#                 result = str(1) + result
#             if r == 10:
#                 result = str(2) + result
#             if r == 11:
#                 result = str(3) + result
#             if r == 100:
#                 result = str(4) + result
#             if r == 101:
#                 result = str(5) + result
#             if r == 110:
#                 result = str(6) + result
#             if r == 111:
#                 result = str(7) + result
#             if r == 1000:
#                 result = str(8) + result
#             if r == 1001:
#                 result = str(9) + result
#             if r == 1010:
#                 result = 'A' + result
#             if r == 1011:
#                 result = 'B' + result
#             if r == 1100:
#                 result = 'C' + result
#             if r == 1101:
#                 result = 'D' + result
#             if r == 1110:
#                 result = 'E' + result
#             if r == 1111:
#                 result = 'F' + result
#             n = n // 10000
#     if base == 8:
#         while n > 0:
#             r = n % 1000
#             if r == 0:
#                 result = str(0) + result
#             if r == 1:
#                 result = str(1) + result
#             if r == 10:
#                 result = str(2) + result
#             if r == 11:
#                 result = str(3) + result
#             if r == 100:
#                 result = str(4) + result
#             if r == 101:
#                 result = str(5) + result
#             if r == 110:
#                 result = str(6) + result
#             if r == 111:
#                 result = str(7) + result
#             n = n // 1000
#     if base == 4:
#         while n > 0:
#             r = n % 100
#             if r == 0:
#                 result = str(0) + result
#             if r == 1:
#                 result = str(1) + result
#             if r == 10:
#                 result = str(2) + result
#             if r == 11:
#                 result = str(3) + result
#             n = n // 100
#     return result
#
#
# print(direct_translation(11001000, 16))
# print(direct_translation(11001000, 8))
# print(direct_translation(11001000, 4))
#
a=4**2016-2**2018+8**800-80
print(bin(a)[2:].count('1'))


def toBase(n,base):
    result='' #v1
    #    #result=[] #v2   if base>9
    while n>0:
        result=str(n%base)+result #v1
        #result.insert(0, n%base) #v2
        n//=base
    return  result
for x in range(100):
    if (1*x**2+2*x**1+1 +1)==(1*7**2+1):
        n=x
print(toBase(n,3))

