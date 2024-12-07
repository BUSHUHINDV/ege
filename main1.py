# b = 1
# for i in range(6080068, 6080177):
#     kol_del = 0
#
#     for j in range(2, i//2+1):
#         if i % j == 0:
#             kol_del += 1
#         if kol_del == 0:
#             print(b, i)
#             break
#     b += 1
a=36
b=-4
c=5
x=((a-b)*c+b*c-(a+b*c*2)*(a+b+1))
print(x%11)