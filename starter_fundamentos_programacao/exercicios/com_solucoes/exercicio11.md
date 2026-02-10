# Exercício 11

## Enunciado

Escrever um algoritmo que leia um valor inteiro do intervalo [0,999] e escreva esse valor por extenso.

## Solução 1

```py

numeros_0a19 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
numeros_dezenas = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem')
numeros_centenas = ('cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos')

num = int(input("Digite u numero inteiro entre 0 e 999: "))

foi = False
if(num > 100):
    parc = num // 100
    print(numeros_centenas[parc - 1], end="")
    num %= 100
    foi = True
if(num > 19):
    if(foi):
        print(" e ", end="")
    parc = num // 10
    print(numeros_dezenas[parc - 2], end="")
    num %= 10
    foi = True
if( num > 0 or not foi):
    if(foi):
        print(" e ", end="")
    print(numeros_0a19[num], end="")

print("\n\n\n") #só por estética

```

## Solução 2

```py
numerosA = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
numerosB = ('vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem')
numerosC = ('cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos')

num = -1
while num < 0 or num > 999:
    try:
        num = int(input('Digite um número entre 0 e 999: '))
    except:
        pass


print(f'Você digitou o número ')
if(num == 0):
    print(numerosA[0])
else:
    if(num > 100):#Tem centena (pq cem é separado tbm)
        parc = num // 100
        print(numerosC[parc - 1], end = '')
        num %= 100
        if(num > 0):
            print(" e ", end = '')
    if(num > 19):#tem dezena maior que 1
        parc = num //10
        print(numerosB[parc - 2], end = '')
        num %= 10
        if(num > 0):
            print(" e ", end = '')
    if(num > 0):
        print(numerosA[num], end = '')

print("\n\n")#só pra quebrar umas linhas
```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.14 - Bom Princípio - RS

♪ Otherside - Red Hot Chili Peppers

Curso: **Fundamentos de Programação**
