def calcular_percentuais(faturamento_por_estado):
    # Calcula o valor total de faturamento
    total_faturamento = sum(faturamento_por_estado.values())
    
    # Calcula o percentual de cada estado
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_por_estado.items()}
    
    return percentuais

def main():
    # Valores de faturamento por estado
    faturamento_por_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    percentuais = calcular_percentuais(faturamento_por_estado)
    
    # Exibe os percentuais de representação
    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
