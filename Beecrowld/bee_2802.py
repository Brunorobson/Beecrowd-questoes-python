n = int(input())

calculo_par = (n * (n -1))/2
calculo_quadrupla = (n*(n-1)*(n-2)*(n-3))/(4*3*2)
resultado = 1 + calculo_par + calculo_quadrupla

print(resultado)