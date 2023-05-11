from random import randint, choice
from math import trunc

alfabeto = []

for minusculas in range(97, 123):
  alfabeto.append(minusculas)
for maiusculas in range(65, 91):
  alfabeto.append(maiusculas)

caracteres_especiais = [33, 35, 36, 37, 38, 63, 64, 95, 45, 42]
caracteres = int(input("Numero de caracteres: "))
while True:
  especiais = input("Caracteres especiais? [S/N]").strip().upper()[0]
  if especiais in 'SN':
    break
  else:
    print("Tente novamente. ", end="")
maximo_especias = trunc(caracteres / 3)
maximo_numeros = trunc(caracteres / 3)
senha_lista = []
numeros = []

while len(senha_lista) < caracteres:
  aleatorio = randint(0, 2)
  numero = randint(0, 9)
  if aleatorio == 0:
    senha_lista.append(chr(choice(alfabeto)))
  elif aleatorio == 1 and maximo_especias > 0 and especiais == 'S':
    senha_lista.append(chr(choice(caracteres_especiais)))
    maximo_especias -= 1
  elif aleatorio == 2 and maximo_numeros > 0:
    if numero not in numeros:
      maximo_numeros -= 1
      senha_lista.append(str(numero))
    numeros.append(numero)
senha = ''.join(senha_lista)

print(f"senha : {senha}")
