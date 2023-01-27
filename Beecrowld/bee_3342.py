n = int(input())
calculo = n*n
if calculo % 2 == 0:
    print(int(calculo/2), 'casas brancas e', int(calculo/2), 'casas pretas')
else:
    print(int((calculo/2)+1), 'casas brancas e',int(calculo/2), 'casas pretas')