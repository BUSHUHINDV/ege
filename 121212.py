#f = open('C:/Users/qwe/Desktop/вариант 36585/17-4.txt','r')
k=0
s=0
d=0
with open("C:/Users/qwe/Desktop/вариант 36585/17-4.txt", "r") as f:
    for line in f.readlines():
        g= int(line)
        if (g % 3 ==0) and (g % 9 !=0) and (g%10>=4):
            k+=1
            s+=g
d=s/k
print('cр=',d,'кол=',k)