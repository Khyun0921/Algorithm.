A = int(input())
result = 1
if A > 0:
    for i in range(1, A+1):
        result *= i
print(result)