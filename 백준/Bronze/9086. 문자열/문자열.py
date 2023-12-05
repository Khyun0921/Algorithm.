import sys
T = int(sys.stdin.readline())
for _ in range(T):
    Str = sys.stdin.readline().rstrip()
    print(Str[0]+Str[-1])