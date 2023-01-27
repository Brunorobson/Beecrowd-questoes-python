n = []
count = 0
x = int(input())
for i in range(x):
    n.append(input())
for entrada in n:
    count = count + 1
    print('resposta %d: %s'%(count ,entrada))