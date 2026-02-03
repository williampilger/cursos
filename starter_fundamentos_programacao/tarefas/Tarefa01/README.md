# Tarefa 1

## Objetivos

- Extrair dados de um arquivo CSV;
- Realizar operações para manipular, e organizar a informação extraída;
- Gerar um relatório simples com os dados processados;
- Exibir um gráfico básico para visualização dos dados.

## Enunciado

Você recebeu um arquivo CSV contendo dados das transações bancárias (incluindo mercado, despesas com o carro, seguro, energia, telefone, vestuário, etc.) de uma família ao longo de um ano.
Cada linha do arquivo contém a seguinte informação: `Data`, `Descrição`, `Categoria`, `Valor` (entrada se positivo, despesa se negativo) e o `Centro de Custo` (que representa *para quem* foi o gasto, ou *de quem* veio a receita, como `Romeu`, `Julieta`, `Família`, `Filho`, etc.).

Elabore um programa que:
1. Leia o arquivo CSV e extraia os dados;
2. Calcule o total de despesas e receitas mês a mês;
3. Calcule o total de despesas por categoria (por exemplo, quanto foi gasto em `mercado`, `carro`, `energia`, etc.);
4. Gere um relatório simples que mostre os totais calculados no passo 2 e 3;
5. Exiba um gráfico básico (usando uma biblioteca como Matplotlib) para visualizar as despesas por categoria.

Seu arquivo CSV está [aqui](./transacoes_familia.csv).


## Dicas

Utilize a biblioteca `csv` do Python para facilitar a leitura do arquivo CSV.

**Veja como ler um arquivo CSV:**

```py
import csv

transacoes = []
with open('transacoes_familia.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) # Cada row é uma lista com os valores das colunas

        # Quebre os dados conforme necessário
        data = row[0]
        descricao = row[1]
        categoria = row[2]
        valor = float(row[3])
        centro_custo = row[4]

        transacoes.append({
            'data': data,
            'descricao': descricao,
            'categoria': categoria,
            'valor': valor,
            'centro_custo': centro_custo
        })

# Agora você pode processar os dados em `transacoes`
print(transacoes) # Visualizando o que foi extraído
```


Use a biblioteca `matplotlib` para criar gráficos simples.

**Veja como usar Matplotlib para criar um gráfico de barras:**

```py
import matplotlib.pyplot as plt
categorias = ['mercado', 'carro', 'energia', 'telefone']
valores = [500, 300, 150, 100]
plt.bar(categorias, valores)
plt.xlabel('Categorias')
plt.ylabel('Despesas')
plt.title('Despesas por Categoria')
plt.show()
```

A documentação oficial do Matplotlib pode ser encontrada [aqui](https://matplotlib.org/stable/contents.html).



## Solução

Veja um exemplo de solução no arquivo [solucao.py](./solucao.py).

```
⚠️ Atenção

No momento, esta solução foi gerada por IA e não foi revisada.
Não se baseie fielmente neste conteúdo. Obrigado pela compreensão!
```


## Sobre

By: **will.i.am** | github.com/williampilger
2026.02.03 - Bom Princípio - RS