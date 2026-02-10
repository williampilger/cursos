# Exercício 14

## Enunciado

Escreva um jogo de adivinhação, onde o usuário tem uma quantidade de tentativas limitadas a 5 chutes para tentar acertar qual o número secreto. O número deve estar entre 0 e 100 e deve ser sorteado aleatoriamente cada vez que o jogo iniciar. A cada tentativa exibir se o número é maior ou menor que o esperado, e interromper a execução quando o número correto for informado ou a quantidade de tentativas for esgotada.

## Solução

```py
import random

print("Este é um jogo de adivinhação!")

numero = random.randrange(1,101)

nivel = 0
print("(1) Fácil\n(2) Médio\n(3) Difícil")
nivel = int(input("Escolha seu nível"))

if(nivel == 1):
    tentativas = 20
elif(nivel == 2):
    tentativas = 10
else:
    tentativas = 5

pontos = 1000

for rodada in range(1, tentativas + 1):
    if(rodada == 1):
        print("Faça sua aposta, ", end="")
    else:
        print("Tente novamente, ", end="")
    print(f"digite um número entre 1 e 100 (tentativa {rodada} de {tentativas}): ", end="")
    chute = int(input(""))

    if(chute < 1 or chute > 100):
        print("Número fora do intervalo!")
        erro_anterior = abs(numero - chute)
        continue

    if(chute == numero):
        print("Mas aah, você acertou!!\n Sua pontuação é de {} de 1000 pontos".format(pontos))
        break
    else:
        erro = abs(numero - chute)
        if(rodada == 1):
            print("Noop. O número secreto é", end=" ")
            if(chute > numero):
                print("menor!")
            else:
                print("maior!")
        elif(rodada < tentativas):
            print("Ainda não.", end=" ")
            if(erro < erro_anterior):
                print("Mas você está mais perto!")
            elif(erro > erro_anterior):
                print("Está esfriando...")
        else:
            print("Eh, infelizmente não foi dessa vez.\nO número secreto era", numero)
        erro_anterior = erro
    pontos -= erro_anterior #erro_anterior sendo usado por que se ele chutar um número fora do intervalo só o erro_anterior é definido



print("Fim de jogo!")


```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.28 - Bom Princípio - RS

♪ Renata - Tihuana

Curso: **Fundamentos de Programação**
