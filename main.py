from random import randint, choice
from math import trunc

alfabeto = [
  'a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
caracteres_especiais = ['!', '@', '#', '$', '%', '&']
caracteres = int(input("Numero de caracteres: "))
especiais = input("Caracteres especiais? [S/N]").strip().upper()[0]
maximo_especias = trunc(caracteres / 3)
maximo_numeros = trunc(caracteres / 3)
contador = 1
senha_lista = []
numeros = []

while len(senha_lista) < caracteres:
  aleatorio = randint(0, 2) == 0
  numero = randint(0, 9)
  letra = choice(alfabeto)
  especial = choice(caracteres_especiais)
  if aleatorio == 0:
    if randint(0, 1) == 0:
      senha_lista.append(letra.upper())
      alfabeto.pop(alfabeto.index(letra))
    else:
      senha_lista.append(letra)
      alfabeto.pop(alfabeto.index(letra))
    contador += 1
  elif aleatorio == 1 and maximo_especias > 0 and especiais == 'S':
    senha_lista.append(especial)
    caracteres_especiais.pop(caracteres_especiais.index(especial))
    maximo_especias -= 1
    contador += 1
  elif aleatorio == 2 and maximo_numeros > 0:
    if numero not in numeros:
      maximo_numeros -= 1
      senha_lista.append(str(numero))
      contador += 1
    numeros.append(numero)
senha = ''.join(senha_lista)

print(f"senha : {senha}")
