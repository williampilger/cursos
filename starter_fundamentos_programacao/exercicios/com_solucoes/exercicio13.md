# Exercício 13

## Enunciado

Elabore um programa para ler um arquivo de texto.txt e contar o número de caracteres contidos no mesmo. Faça também a contagem da quantidade de vezes que cada letra/número foi encontrado.

## Solução

```py
nomeArquivo = "noticia.txt"
contagem = {}
total_caracteres = 0
with open(nomeArquivo, "rt") as arquivo:
    for linha in arquivo:
        for letra in linha:
            if(not letra in contagem):
                contagem[letra] = 1
            else:
                contagem[letra] += 1
            total_caracteres += 1

print(f" Foram contados {total_caracteres} caracteres no arquivo {nomeArquivo}.")

for item in sorted(contagem):
print(f"{item} apareceu {contagem[item]} vezes.")
```

## Sobre

By: **will.i.am** | github.com/williampilger

2021.11.27 - Bom Princípio - RS

♪ Só os Loucos Sabem - Charlie Brown Jr.

Curso: **Fundamentos de Programação**
