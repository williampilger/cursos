# Exercício 07.1

## Enunciado

Elabore um programa que lê 10 valores inteiros.
Ao final, escreva o menor e o maior valor.

## Solução 1

```py
n = 0
while n < 10:
    number = int(input(f'Digite o número {n+1} de 10: '))
    if n == 0:
        max = min = number
    else:
        if number > max:
            max = number
        if number < min:
            min = number
    n = n + 1

print(f'O maior número é: {max}')
print(f'O menor número é: {min}')
```

## Solução 2

```py
for n in range(10):
    number = int(input(f'Digite o número {n+1} de 10: '))
    if n == 0:
        max = min = number
    else:
        if number > max:
            max = number
        if number < min:
            min = number

print(f'O maior número é: {max}')
print(f'O menor número é: {min}')
```

## Solução 3

```py
max = float('-inf')
min = float('inf')

n = 0
while n < 10:
    number = int(input(f'Digite o número {n+1} de 10: '))
    if number > max:
        max = number
    if number < min:
        min = number
    n = n + 1

print(f'O maior número é: {max}')
print(f'O menor número é: {min}')
```
