# f=open('C:/Users/qwe/Downloads/24_7600.txt')
# # a=['Q','R','S']
# # s=f.readline()
# # k=1
# # kmax=0
# # s2=''
# # for i in range(len(s)):
# #     if s[i] in a:
# #         s2+='*'
# #     else:
# #         s2+=s[i]
# # print(s2)
# # for i in range(len(s)-1):
# #     if (s2[i]=='*')and(s2[i+1]=='*'):
# #         kmax=max(k,kmax)
# #         k=1
# #     else:
# #         k+=1
# # print(kmax)

f=open('2025_24.txt')
s=''
tmp=''
l=[]
nach=0
s=f.readline()
# print(s,len(s))
for i in s:
    if nach==0 and (i not in '0*-'):
        nach=1
        tmp+=i
        #continue
    if nach == 1 and (tmp[-1] in '*-') and (i in '*-'):
        nach = 0
        l.append(tmp)
        tmp = ''
    if nach==1 :
        tmp+=i
        #continue

for i in l:
    if len(i)>10:
        print(i)
