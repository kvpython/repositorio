"""
 O mercado seu jose esta com uma promoção de 10% para seus clientes de 18 anos.
 faça um progama em python a idade, o valor total e mostre se ele pode ou 
 não receber o desconto. Qual o desconto e o valor total.
"""
import os
os.system ('clear')

idade = int(input("digite sua idade \n"))
total = float(input("digite o valor total dos protudos \n"))

if (idade>=18):
    print("pode ter o desconto")
    desconto = total * 0.1
    final = total - desconto
    print(f"seu desconto foi de R${desconto} e o valor final é de R${final}")

else:
    print("voce não tem direito a este desconto, seu valor final é de R$c{total}" )
       
