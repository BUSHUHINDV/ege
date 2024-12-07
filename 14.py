# def f(n):
#     if n==0:
#         return 0
#     elif n > 0 and n%2==0:
#         return f(n/2)
#     elif n > 0 and n % 2 !=0:
#         return 1+f(n-1)
# for x in range (500):
#     if f(x)==8:
#         print(x)
# #print(f(100))


# for x in range(19):
#     n1=9*19**7+8*19**6+8*19**5+9*19**4+7*19**3+x*19**2+2*19+1
#     n2=2*19**4+x*19**3+9*19**2+2*19+3
#     if (n1+n2)%18==0:
#         print (x,(n1+n2)//18)



# n=3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2024
# a=[]
# while n>0:
#     a.append(n%25)
#     n=n//25
# print(a)


for a in range(1,1000):
    F=1
    for x in range(1,100):
        for y in range(1,100):
           q=((x+2*y)<a)or(y>x)or(x>60)
           if q==False:
               F=0
    if F==1:
        print(a)
