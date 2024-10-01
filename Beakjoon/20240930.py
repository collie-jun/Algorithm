# 백준 2675

a = int(input())
for i in range(a):
  b, c = input().split()
  for i in range(len(c)):
    print(int(b) * c[i], end='')
  print()

  