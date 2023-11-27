A = input().upper()
A_list = list(set(A))
B = []
for i in A_list:
  count = A.count
  B.append(count(i))
if B.count(max(B)) > 1:
  print("?")
else:
  print(A_list[(B.index(max(B)))])
