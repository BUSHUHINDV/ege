#f=open('C:/Users/qwe/Downloads/17-9 (1).txt')
#a=[]
#for i in f:
#    a.append(int(i))
#print(a)
#k=0
#m=0
#for i in range (len(a)-2):
#    s1=bin(a[i])[2:]
#    s2 = bin(a[i+1])[2:]
#    s3 = bin(a[i+2])[2:]
#    if (s1.count('1')>2 and s1.count('0')>0 and s2.count('1')>2 and s2.count('0')>0) \
#            or(s3.count('1')>2 and s3.count('0')>0 and s2.count('1')>2 and s2.count('0')>0) \
#            or (s1.count('1')>2 and s1.count('0')>0 and s3.count('1')>2 and s3.count('0')>0):
#        k+=1
#        m=max(a[i],a[i+1],a[i+2],m)
#    #print(a[i],a[i+1],a[i+2])
#print(k,m)
'''
8	(№ 4249) (А. Куканова) Лиля составляет 5-буквенные слова из букв С, О, Т, К, А, П, Л, З. Слово не должно заканчиваться на гласную и содержать сочетания ЗЛО. Буквы в слове не повторяются. Сколько слов может составить Лиля?
Спрятать ответ

5008
'''

k=1
for a in 'соткаплз':
    for b in 'соткаплз':
        for c in 'соткаплз':
            for d in 'соткаплз':
                for e in 'соткаплз':
                    s=a+b+c+d+e
                    if s.count('зло')==0 and s[-1]!='о' and s[-1]!='а' and s.count('с')<=1 and s.count('о')<=1 and s.count('т')<=1 and s.count('к')<=1 and s.count('а')<=1 and s.count('п')<=1 and s.count('л')<=1 and s.count('з')<=1:
                        print(k,s)
                        k+=1




