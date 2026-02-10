# Exercício 03

## Enunciado

Elabore um script que leia um número inteiro de três digitos, informado pelo usuário, e em seguida some seus algarismos, exibindo o resultado ao final. Ex.: 569 = 20.

## Solução

```py

valor = int(input("Digite o número: "))

a = valor % 10
valor = int(valor/10)
b = valor % 10
c = int(valor / 10)

soma = a+b+c
print(f"A soma dos digitos é : {soma}")

```

obs.: Este algoritmo não é dinâmico, ou seja, não poderá ser usado para somar os dígitos de um número que não tenha **exatamente três dígitos**, em exercícios futuros veremos laços de repetição, e iremos melhorar este algoritmo.

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.13 - Bom Princípio - RS

♪ Whatever It Takes - Imagine Dragons

Curso: **Fundamentos de Programação**