n = int(input())
for _ in range(n):
    a = input()
    if len(a) >= 6 and len(a) <= 9:
        print('yes')
    else:
        print('no')