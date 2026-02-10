# Exercício 08

## Enunciado

Elabore um programa que lê valores para um vetor de 10 posições e o escreve. Escreve, a seguir, somente os números primos deste vetor.

## Solução

```py

def eh_primo(valor):
    if(valor > 0):
        contagem = 2 #todo número é divisível por 1 e por ele mesmo.
        for i in range(2,valor):
            if(valor % i == 0):
                contagem += 1
        if(contagem == 2):
            return True
    return False

from random import random #vamos usar números aleatórios, para facilitar nossa vida

vetor = []
for i in range(10):
    vetor.append(int(random()*100))

print(vetor)

for valor in vetor:
    if(eh_primo(valor)):
        print(valor)

```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.13 - Bom Princípio - RS

♪ Anastasia - Slash

Curso: **Fundamentos de Programação**
