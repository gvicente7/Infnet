# -*- coding: utf-8 -*-
"""Gabriel_Vicente_DR1_TP3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gMWAboaLAAGHQrL9cR6D2A0-4KZuiV9J
"""

#Questão 1

valor_valido = True
percentual = 0
pessoas = 0
conta_total_formatada = "0,00"

valor = float(input("Informe o valor total do consumo: R$ "))
percentual = float(input("Informe o percentual do serviço, entre 0 e 100:"))
if percentual >= 0 and percentual <= 100:
  pessoas = int(input("Informe o total de pessoas:"))
  if pessoas > 0 and valor_valido == True:
    conta_total = round(((valor * (percentual/100))+valor),2)
    conta = str(round(conta_total/pessoas,2)).replace(".",",")
    conta_total_formatada = str(conta_total).replace(".",",")
    print(f"O valor total da conta, com a taxa de serviço, será de R$ {conta_total_formatada}")
    print(f"Dividindo a conta por 2 pessoa(s), cada pessoa deverá pagar R$ {conta}")
  else: print("Valor invalido.")
else:
  print("Valor invalido.")

#Questão 2

idade_valida = True

idade = int(input("Informe a idade:"))
if (idade >= 16 and idade < 18) or idade > 70:
  print("Eleitor facultativo")
else:  
  if idade >= 18 and idade <=70:
      print("Eleitor obrigatório")
  else:
    if idade < 16 and idade >= 0:
      print("Não tem direito a voto") 
    else:
      if idade < 0:
        print("Idade inválida.")

#Questão 3
Nota_valido = True

Nome_1 = input("Informe nome do 1º participante: ")
Nota_1 = float(input("Informe nota do 1º participante: "))
if Nota_1 < 0 or Nota_1 > 10:
  Nota_valido = False
else:
  Nome_2 = input("Informe nome do 2º participante: ")
  Nota_2 = float(input("Informe nota do 2º participante: "))
  if Nota_2 < 0 or Nota_2 > 10:
    Nota_valido = False
  else:
    Nome_3 = input("Informe nome do 3º participante: ")
    Nota_3 = float(input("Informe nota do 3º participante: "))
    if Nota_3 < 0 or Nota_3 > 10:
      Nota_valido = False
    else:
      Nome_4 = input("Informe nome do 4º participante: ")
      Nota_4 = float(input("Informe nota do 4º participante: "))
      if Nota_4 < 0 or Nota_4 > 10:
        Nota_valido = False
      else:
        Nome_5 = input("Informe nome do 5º participante: ")
        Nota_5 = float(input("Informe nota do 5º participante: "))
        if Nota_5 < 0 or Nota_5 > 10:
          Nota_valido = False


if Nota_valido == False:
  print("Nota inválida.")
else:
  if Nota_1 > Nota_2 and Nota_1 > Nota_3 and Nota_1 > Nota_4 and Nota_1 > Nota_5:
    print(f"O(a) vencedor(a) foi {Nome_1} com nota {Nota_1}!")
  else:
    if Nota_2 > Nota_1 and Nota_2 > Nota_3 and Nota_2 > Nota_4 and Nota_2 > Nota_5:
      print(f"O(a) vencedor(a) foi {Nome_2} com nota {Nota_2}!")
    else:
      if Nota_3 > Nota_2 and Nota_3 > Nota_1 and Nota_3 > Nota_4 and Nota_3 > Nota_5:
        print(f"O(a) vencedor(a) foi {Nome_3} com nota {Nota_3}!")
      else:
        if Nota_4 > Nota_2 and Nota_4 > Nota_3 and Nota_4 > Nota_1 and Nota_4 > Nota_5:
          print(f"O(a) vencedor(a) foi {Nome_4} com nota {Nota_4}!")
        else:
          print(f"O(a) vencedor(a) foi {Nome_5} com nota {Nota_5}!")