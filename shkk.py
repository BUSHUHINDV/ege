num1=int(input())
num2=int(input())

number=abs(num1)
count=0#abs(num1)
result=0
while count<abs(num2):
    result+=number
    count+=1
if (num1<0) ^ (num2<0):
    print(-result)
else:
    print(result)