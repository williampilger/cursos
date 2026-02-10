# Exercício 05

## Enunciado

Escreva um algoritmo que leia um valor inteiro e diga se ele é primo.

## Solução

```py

a = int(input("Digite um numero inteiro: "))

cont = 0
for i in range(2, a // 2):
    if( a % i == 0):
        cont += 1
        break

if(cont == 0):
    print("é primo")
else:
    print("não é primo")

```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.13 - Bom Princípio - RS

♪ Final Masquerade - Linkin Park

Curso: **Fundamentos de Programação**
