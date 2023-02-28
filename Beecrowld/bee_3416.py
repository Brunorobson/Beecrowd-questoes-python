N, L, D = map(int, input().split())
quantidade_de_café = (N * D)//L
if (N*D) % L != 0:
  quantidade_de_café += 1
print(quantidade_de_café)