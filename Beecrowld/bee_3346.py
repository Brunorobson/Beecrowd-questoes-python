ano1, ano2 = map(float, input().split())
resposta = (100 + ano1)*(ano2/100+1)-100
print(f'{resposta:.6f}')