# Exercício 10

## Enunciado

Elabore um programa para ler valores para dois vetores, a[5] e b[5]. Transfira, a seguir, os valores lidos para um vetor c[10] e os escreva de maneira ordenada.

## Solução 01

Neste exercício temos duas grandes maneira de fazer isso. A primeira é a utilização de loops e a ordenação "manual" dos valores, já na **Solução 2** veremos como utilizar funções (ou métodos) do python para facilitar este processo.

```py

n = 5#número de valores a ser preenchido por vetor

#Coleta dos valores
a = []
for i in range(n):
    a.append(float(input(f"Digite o {i+1}º valor para o vetor a: ").replace(',','.')))
b = []
for i in range(n):
    b.append(float(input(f"Digite o {i+1}º valor para o vetor b: ").replace(',','.')))

#Criação de C
c = []
for i in range(n): #existem N outras formas de fazer isso, e assim só é possível por A e B terem o mesmo tamanho
    c.append(a[i])
    c.append(b[i])

#Ordenar e printar
for i in range(n * 2):
    for j in range(n * 2):
        if( c[i] < c[j]):
            aux = c[i]
            c[i] = c[j]
            c[j] = aux

print(f"O vetor ordenado é:\n {c}")

```

## Solução 2

```py

n = 5

#Coleta de dados
a = []
for i in range(n):
    a.append(float(input(f"Digite o {i+1}º valor para o vetor a: ").replace(',','.')))
b = []
for i in range(n):
    b.append(float(input(f"Digite o {i+1}º valor para o vetor b: ").replace(',','.')))

#Criação de C
c = []
for i in range(n):
    c.append(a[i])
    c.append(b[i])

#Ordenar e printar
print("O vetor ordenado é:")
print(sorted(c))

```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.14 - Bom Princípio - RS

♪ Runnin' - Adam Lambert

Curso: **Fundamentos de Programação**
