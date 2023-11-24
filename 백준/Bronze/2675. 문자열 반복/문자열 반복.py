n=int(input())

for _ in range(n):
    t,w = input().split()
    t=int(t)
    ri=""
    for i in w:
        ri +=i*t
    print(ri)
