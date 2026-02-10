# Exercício 06

## Enunciado

Escrever um algoritmo que leia dois valores inteiros e escreva a lista dos valores inteiros do primeiro até o segundo valor, e se o primeiro for maior que o segundo, a ordem deve ser decrescente. Se os valores forem iguais, escrever “valores iguais”.

## Solução

```py

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

if(valor1 == valor2):
    print("Valores iguais!")
else:
    if(valor1 < valor2):
        rg = range(valor1, valor2 + 1)
    else:
        rg = range(valor1, valor2 - 1, -1)
    for numero in rg:
        print(numero)

```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.13 - Bom Princípio - RS

♪ Só uma Canção - Barbarella

Curso: **Fundamentos de Programação**
