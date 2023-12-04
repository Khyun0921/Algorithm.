A = [i for i in range(1,31)]
for i in range(28):
    applied = int(input())
    A.remove(applied) 
print(min(A))
print(max(A))
