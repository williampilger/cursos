# Exercício 09

## Enunciado

Elabore um programa que lê 10 valores inteiros para um vetor. Encontre o menor e o maior valor deste vetor, escrevendo-os juntamente com a sua posição.

## Solução

```py

from random import random

for i in range(10):
    valor = int(random()*100)
    if(i == 0): #primeira vez
        maior = valor
        maior_index = 0
        menor = valor
        menor_index = 0
    else:
        if(valor > maior):
            maior = valor
            maior_index = i
        elif(valor < menor):
            menor = valor
            menor_index = i
    print(valor)

print(f"O maior valor é {maior}, e está na posição {maior_index}")
print(f"O menor valor é {menor}, e está na posição {menor_index}")

```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.13 - Bom Princípio - RS

♪ Teenagers - My Chemical Romance

Curso: **Fundamentos de Programação**
