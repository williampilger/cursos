# Exercício 07

## Enunciado

Faça um algoritmo que leia vários números inteiros e calcule o somatório dos números negativos. O fim da leitura será indicado pelo número 0. Mostrar o resultado final.

## Solução

```py

soma = 0
while True:
    valor = int(input("Digite um valor: "))
    if(valor == 0):
        break
    if(valor < 0):
        soma += valor

print(f"A soma dos negativos é: {soma}")

```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.13 - Bom Princípio - RS

♪ Numb - Linkin Park

Curso: **Fundamentos de Programação**
