a='1'*20
b='2'*15
c='3'*40
f='>'+a+b+c+'<'
print(f)
while '><' not in f:
    f=f.replace('>1','3>',1)
    f=f.replace('>2', '2>', 1)
    f=f.replace('>3', '1>', 1)
    f=f.replace('3<', '<1', 1)
    f=f.replace('2<', '<3', 1)
    f=f.replace('1<', '<2', 1)
print(f)
s=0
for i in f:
    try:
        s=s+int(i)
    except:
        i=0
print(s)

f='>'+a+c+b+'<'
print(f)
while '><' not in f:
    f=f.replace('>1','3>',1)
    f=f.replace('>2', '2>', 1)
    f=f.replace('>3', '1>', 1)
    f=f.replace('3<', '<1', 1)
    f=f.replace('2<', '<3', 1)
    f=f.replace('1<', '<2', 1)
print(f)
s=0
for i in f:
    try:
        s=s+int(i)
    except:
        i=0
print(s)

f='>'+b+a+c+'<'
print(f)
while '><' not in f:
    f=f.replace('>1','3>',1)
    f=f.replace('>2', '2>', 1)
    f=f.replace('>3', '1>', 1)
    f=f.replace('3<', '<1', 1)
    f=f.replace('2<', '<3', 1)
    f=f.replace('1<', '<2', 1)
print(f)
s=0
for i in f:
    try:
        s=s+int(i)
    except:
        i=0
print(s)

f='>'+c+a+b+'<'
print(f)
while '><' not in f:
    f=f.replace('>1','3>',1)
    f=f.replace('>2', '2>', 1)
    f=f.replace('>3', '1>', 1)
    f=f.replace('3<', '<1', 1)
    f=f.replace('2<', '<3', 1)
    f=f.replace('1<', '<2', 1)
print(f)
s=0
for i in f:
    try:
        s=s+int(i)
    except:
        i=0
print(s)

f='>'+c+b+a+'<'
print(f)
while '><' not in f:
    f=f.replace('>1','3>',1)
    f=f.replace('>2', '2>', 1)
    f=f.replace('>3', '1>', 1)
    f=f.replace('3<', '<1', 1)
    f=f.replace('2<', '<3', 1)
    f=f.replace('1<', '<2', 1)
print(f)
s=0
for i in f:
    try:
        s=s+int(i)
    except:
        i=0
print(s)

f='>'+b+c+a+'<'
print(f)
while '><' not in f:
    f=f.replace('>1','3>',1)
    f=f.replace('>2', '2>', 1)
    f=f.replace('>3', '1>', 1)
    f=f.replace('3<', '<1', 1)
    f=f.replace('2<', '<3', 1)
    f=f.replace('1<', '<2', 1)
print(f)
s=0
for i in f:
    try:
        s=s+int(i)
    except:
        i=0
print(s)