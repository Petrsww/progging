s=input().split()
g=int(s[0])
st=s[1]
l=len(st)
num=l//g
a=[]
for i in range(num):
    a.append(st[i*g:(i+1)*g])
b=[]
for j in range(len(a)):
    b.append(a[j][::-1])
r=''.join(b)
print(r)