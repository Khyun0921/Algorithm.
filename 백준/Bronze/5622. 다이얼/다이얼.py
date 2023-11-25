s=input()
t='22233344455566677778889999'
r=0
for a in s:
    r+=int(t[ord(a)-65])+1
print(r)