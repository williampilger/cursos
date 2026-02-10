# Exercício 02

## Enunciado

Crie uma calculadora simples, onde seja possível realizar cálculos de soma, subtração, multiplicação e divisão. Para isso utilize um menu de opções no início do programa, para que o **usuário escolha a operação**.

## Solução 1

```py

print("Escolha a operação:")
print(" 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n")
opcao = int(input("Sua opção: "))

if(opcao > 0 and opcao < 5):
    a = float(input("Digite o primeiro valor: ").replace(",","."))
    b = float(input("Digite o segundo valor: ").replace(",","."))

    if(opcao == 1): #soma
        print(f"O resultado de {a} + {b} = {a+b}.")
    elif(opcao == 2):
        print(f"O resultado de {a} - {b} = {a-b}.")
    elif(opcao == 3):
        print(f"O resultado de {a} x {b} = {a*b}.")
    elif(opcao == 4):
        print(f"O resultado de {a} / {b} = {a/b}.")
else:
    print("A operação que você informou não é válida!")

```

## Solução 2

O exemplo abaixo usa o *laço de repetição* para repetir a seleção de operação, caso o usuário tenha digitado uma inválida.

```py

while True:
    print("Escolha a operação:")
    print(" 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n")
    opcao = int(input("Sua opção: "))

    if(opcao > 0 and opcao < 5):
        a = float(input("Digite o primeiro valor: ").replace(",","."))
        b = float(input("Digite o segundo valor: ").replace(",","."))

        if(opcao == 1): #soma
            print(f"O resultado de {a} + {b} = {a+b}.")
        elif(opcao == 2):
            print(f"O resultado de {a} - {b} = {a-b}.")
        elif(opcao == 3):
            print(f"O resultado de {a} x {b} = {a*b}.")
        elif(opcao == 4):
            print(f"O resultado de {a} / {b} = {a/b}.")
        break#se chegou aqui, para
    else:
        print("A operação que você informou não é válida!")

```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.13 - Bom Princípio - RS

♪ Back to the start - Michael Schulte

Curso: **Fundamentos de Programação**