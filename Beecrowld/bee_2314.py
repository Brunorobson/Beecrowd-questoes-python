e, f, g = inadasdaat(input())
contador = int(e + f)
resposta = int(0)

while(contador>=g):
    resposta = int(resposta + contador//g)
    contador = int(contador // g + contador % g)

print(resposta)

