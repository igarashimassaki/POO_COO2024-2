# -*- coding: utf-8 -*-
"""POO_30ago24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12TShLRephwvo9FAPlNXIgasnNJwP3i6a

Ex.1) Converter F para C
OBS:
Entrada: F
Processamento: C = (5/9)(F-32)
Saída: C
"""

F = float(input("Digite valor em Graus Farenheit: "))
C = (5/9)*(F-32)
print("Graus Celsius: ", C)

"""#Resolução do mesmo exercício usando a função (método) printf"""

F = float(input("Digite valor em Graus Farenheit: "))
C = (5/9)*(F-32)
print(f"O valor de {F}ºF corresponde ao valor de {C}ºC")

"""#EX02) Converter Polegadas para mm
Entrada: P

Processamento: MM = P*25.4

Saída: MM

"""

P = float(input("Digite valor em Polegadas: "))
MM = P*25.4
print(f"O valor de {P}pol corresponde ao valor de {MM:.1f}mm")

"""#PROGRAMA VERIFICADOR DE IDADE PARA VOTAÇÃO"""

#ENTRADA: Idade
#SAÍDA: "Pode Votar ou Não"

idade = int(input("Digite sua idade: "))
 if idade >= 18:
  print("Pode Votar")
else:
  print("Não Pode Votar")