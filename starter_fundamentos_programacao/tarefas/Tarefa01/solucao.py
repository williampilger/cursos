"""
Tarefa 1 - Análise de Transações Bancárias
Solução completa para análise financeira de uma família

⚠️ Com exceção desta linha, este conteúdo TODO foi gerado por IA. Cuidado!
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict


def ler_transacoes(nome_arquivo):
    """
    Lê o arquivo CSV e retorna uma lista de transações.
    
    Args:
        nome_arquivo: Nome do arquivo CSV a ser lido
        
    Returns:
        Lista de dicionários contendo as transações
    """
    transacoes = []
    
    with open(nome_arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        
        for row in reader:
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
    
    return transacoes


def calcular_totais_mensais(transacoes):
    """
    Calcula o total de receitas e despesas mês a mês.
    
    Args:
        transacoes: Lista de transações
        
    Returns:
        Dicionário com totais mensais de receitas, despesas e saldo
    """
    totais_mensais = defaultdict(lambda: {'receitas': 0, 'despesas': 0, 'saldo': 0})
    
    for transacao in transacoes:
        # Extrai ano e mês da data (formato: YYYY-MM-DD)
        data = transacao['data']
        ano_mes = data[:7]  # Pega "YYYY-MM"
        
        valor = transacao['valor']
        
        if valor > 0:
            totais_mensais[ano_mes]['receitas'] += valor
        else:
            totais_mensais[ano_mes]['despesas'] += abs(valor)
        
        totais_mensais[ano_mes]['saldo'] = (
            totais_mensais[ano_mes]['receitas'] - totais_mensais[ano_mes]['despesas']
        )
    
    return dict(totais_mensais)


def calcular_despesas_por_categoria(transacoes):
    """
    Calcula o total de despesas por categoria.
    
    Args:
        transacoes: Lista de transações
        
    Returns:
        Dicionário com total gasto por categoria
    """
    despesas_por_categoria = defaultdict(float)
    
    for transacao in transacoes:
        if transacao['valor'] < 0:  # Apenas despesas (valores negativos)
            categoria = transacao['categoria']
            despesas_por_categoria[categoria] += abs(transacao['valor'])
    
    return dict(despesas_por_categoria)


def calcular_despesas_por_centro_custo(transacoes):
    """
    Calcula o total de despesas por centro de custo.
    
    Args:
        transacoes: Lista de transações
        
    Returns:
        Dicionário com total gasto por centro de custo
    """
    despesas_por_centro = defaultdict(float)
    
    for transacao in transacoes:
        if transacao['valor'] < 0:  # Apenas despesas
            centro = transacao['centro_custo']
            despesas_por_centro[centro] += abs(transacao['valor'])
    
    return dict(despesas_por_centro)


def gerar_relatorio(totais_mensais, despesas_por_categoria, despesas_por_centro):
    """
    Gera e exibe um relatório formatado com os dados financeiros.
    
    Args:
        totais_mensais: Dicionário com totais mensais
        despesas_por_categoria: Dicionário com despesas por categoria
        despesas_por_centro: Dicionário com despesas por centro de custo
    """
    print("=" * 80)
    print("RELATÓRIO FINANCEIRO DA FAMÍLIA - ANO 2025".center(80))
    print("=" * 80)
    print()
    
    # Relatório Mensal
    print("📅 RESUMO MENSAL")
    print("-" * 80)
    print(f"{'Mês':<12} {'Receitas':>15} {'Despesas':>15} {'Saldo':>15}")
    print("-" * 80)
    
    total_receitas_ano = 0
    total_despesas_ano = 0
    
    # Ordena os meses cronologicamente
    meses_ordenados = sorted(totais_mensais.keys())
    
    for mes in meses_ordenados:
        dados = totais_mensais[mes]
        receitas = dados['receitas']
        despesas = dados['despesas']
        saldo = dados['saldo']
        
        total_receitas_ano += receitas
        total_despesas_ano += despesas
        
        # Formata o mês para exibição
        ano, mes_num = mes.split('-')
        meses_nomes = ['', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                       'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        mes_nome = f"{meses_nomes[int(mes_num)]}/{ano}"
        
        cor_saldo = "+" if saldo >= 0 else "-"
        print(f"{mes_nome:<12} R$ {receitas:>11,.2f} R$ {despesas:>11,.2f} {cor_saldo} R$ {abs(saldo):>9,.2f}")
    
    print("-" * 80)
    saldo_anual = total_receitas_ano - total_despesas_ano
    cor_anual = "+" if saldo_anual >= 0 else "-"
    print(f"{'TOTAL ANO':<12} R$ {total_receitas_ano:>11,.2f} R$ {total_despesas_ano:>11,.2f} {cor_anual} R$ {abs(saldo_anual):>9,.2f}")
    print()
    
    # Despesas por Categoria
    print("📊 DESPESAS POR CATEGORIA")
    print("-" * 80)
    print(f"{'Categoria':<25} {'Valor Total':>20} {'% do Total':>15}")
    print("-" * 80)
    
    # Ordena categorias por valor (maior para menor)
    categorias_ordenadas = sorted(despesas_por_categoria.items(), 
                                  key=lambda x: x[1], reverse=True)
    
    for categoria, valor in categorias_ordenadas:
        percentual = (valor / total_despesas_ano) * 100
        print(f"{categoria:<25} R$ {valor:>15,.2f} {percentual:>14.1f}%")
    
    print("-" * 80)
    print(f"{'TOTAL':<25} R$ {total_despesas_ano:>15,.2f} {100.0:>14.1f}%")
    print()
    
    # Despesas por Centro de Custo
    print("👥 DESPESAS POR CENTRO DE CUSTO")
    print("-" * 80)
    print(f"{'Centro de Custo':<25} {'Valor Total':>20} {'% do Total':>15}")
    print("-" * 80)
    
    # Ordena centros de custo por valor (maior para menor)
    centros_ordenados = sorted(despesas_por_centro.items(), 
                               key=lambda x: x[1], reverse=True)
    
    for centro, valor in centros_ordenados:
        percentual = (valor / total_despesas_ano) * 100
        print(f"{centro:<25} R$ {valor:>15,.2f} {percentual:>14.1f}%")
    
    print("-" * 80)
    print(f"{'TOTAL':<25} R$ {total_despesas_ano:>15,.2f} {100.0:>14.1f}%")
    print()
    print("=" * 80)


def gerar_grafico_categorias(despesas_por_categoria):
    """
    Gera um gráfico de barras mostrando as despesas por categoria.
    
    Args:
        despesas_por_categoria: Dicionário com despesas por categoria
    """
    # Ordena categorias por valor (maior para menor)
    categorias_ordenadas = sorted(despesas_por_categoria.items(), 
                                  key=lambda x: x[1], reverse=True)
    
    # Separa categorias e valores
    categorias = [cat for cat, _ in categorias_ordenadas]
    valores = [val for _, val in categorias_ordenadas]
    
    # Cria o gráfico
    plt.figure(figsize=(14, 8))
    
    # Gráfico de barras
    barras = plt.bar(categorias, valores, color='steelblue', edgecolor='navy', alpha=0.7)
    
    # Adiciona valores no topo das barras
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura,
                f'R$ {altura:,.0f}',
                ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Configurações do gráfico
    plt.xlabel('Categorias', fontsize=12, fontweight='bold')
    plt.ylabel('Despesas (R$)', fontsize=12, fontweight='bold')
    plt.title('Despesas por Categoria - Ano 2025', fontsize=16, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    # Exibe o gráfico
    plt.show()


def gerar_grafico_mensal(totais_mensais):
    """
    Gera um gráfico de linhas mostrando a evolução mensal de receitas e despesas.
    
    Args:
        totais_mensais: Dicionário com totais mensais
    """
    # Ordena os meses cronologicamente
    meses_ordenados = sorted(totais_mensais.keys())
    
    # Prepara os dados
    meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                   'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    meses_labels = []
    receitas = []
    despesas = []
    saldos = []
    
    for mes in meses_ordenados:
        ano, mes_num = mes.split('-')
        meses_labels.append(f"{meses_nomes[int(mes_num)-1]}")
        
        dados = totais_mensais[mes]
        receitas.append(dados['receitas'])
        despesas.append(dados['despesas'])
        saldos.append(dados['saldo'])
    
    # Cria o gráfico
    plt.figure(figsize=(14, 8))
    
    # Plota as linhas
    plt.plot(meses_labels, receitas, marker='o', linewidth=2, 
             label='Receitas', color='green', markersize=8)
    plt.plot(meses_labels, despesas, marker='s', linewidth=2, 
             label='Despesas', color='red', markersize=8)
    plt.plot(meses_labels, saldos, marker='^', linewidth=2, 
             label='Saldo', color='blue', markersize=8)
    
    # Linha horizontal no zero
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5, alpha=0.3)
    
    # Configurações do gráfico
    plt.xlabel('Mês', fontsize=12, fontweight='bold')
    plt.ylabel('Valor (R$)', fontsize=12, fontweight='bold')
    plt.title('Evolução Mensal - Receitas, Despesas e Saldo - 2025', 
              fontsize=16, fontweight='bold', pad=20)
    plt.legend(fontsize=11, loc='best')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    # Exibe o gráfico
    plt.show()


def gerar_grafico_pizza_categorias(despesas_por_categoria):
    """
    Gera um gráfico de pizza mostrando a distribuição percentual das despesas.
    
    Args:
        despesas_por_categoria: Dicionário com despesas por categoria
    """
    # Ordena categorias por valor (maior para menor)
    categorias_ordenadas = sorted(despesas_por_categoria.items(), 
                                  key=lambda x: x[1], reverse=True)
    
    # Pega as 10 maiores categorias e agrupa o resto em "Outros"
    top_n = 10
    if len(categorias_ordenadas) > top_n:
        top_categorias = categorias_ordenadas[:top_n]
        outros_valor = sum([val for _, val in categorias_ordenadas[top_n:]])
        
        categorias = [cat for cat, _ in top_categorias] + ['Outros']
        valores = [val for _, val in top_categorias] + [outros_valor]
    else:
        categorias = [cat for cat, _ in categorias_ordenadas]
        valores = [val for _, val in categorias_ordenadas]
    
    # Cria o gráfico
    plt.figure(figsize=(12, 8))
    
    # Define cores
    cores = plt.cm.Set3(range(len(categorias)))
    
    # Gráfico de pizza
    wedges, texts, autotexts = plt.pie(valores, labels=categorias, autopct='%1.1f%%',
                                        startangle=90, colors=cores,
                                        textprops={'fontsize': 10})
    
    # Destaca a maior fatia
    wedges[0].set_edgecolor('black')
    wedges[0].set_linewidth(2)
    
    # Configurações
    plt.title('Distribuição de Despesas por Categoria - 2025', 
              fontsize=16, fontweight='bold', pad=20)
    plt.axis('equal')
    plt.tight_layout()
    
    # Exibe o gráfico
    plt.show()


def main():
    """
    Função principal que executa toda a análise.
    """
    # Nome do arquivo CSV
    arquivo_csv = 'transacoes_familia.csv'
    
    print("\n🔍 Lendo arquivo de transações...")
    transacoes = ler_transacoes(arquivo_csv)
    print(f"✅ {len(transacoes)} transações carregadas com sucesso!\n")
    
    print("📊 Processando dados...")
    totais_mensais = calcular_totais_mensais(transacoes)
    despesas_por_categoria = calcular_despesas_por_categoria(transacoes)
    despesas_por_centro = calcular_despesas_por_centro_custo(transacoes)
    print("✅ Dados processados!\n")
    
    # Gera o relatório
    gerar_relatorio(totais_mensais, despesas_por_categoria, despesas_por_centro)
    
    # Gera os gráficos
    print("\n📈 Gerando gráficos...\n")
    
    print("1️⃣ Gráfico de barras - Despesas por Categoria")
    gerar_grafico_categorias(despesas_por_categoria)
    
    print("2️⃣ Gráfico de linhas - Evolução Mensal")
    gerar_grafico_mensal(totais_mensais)
    
    print("3️⃣ Gráfico de pizza - Distribuição de Despesas")
    gerar_grafico_pizza_categorias(despesas_por_categoria)
    
    print("\n✅ Análise concluída!\n")


if __name__ == "__main__":
    main()
