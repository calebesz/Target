def calcular_faturamento(faturamento_diario):
    # Filtra os dias com faturamento (ignora os dias sem faturamento)
    dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
    
    if not dias_com_faturamento:
        return "Nenhum faturamento registrado no mês."
    
    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    
    # Calcula a média mensal, ignorando os dias sem faturamento
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    
    # Conta o número de dias com faturamento superior à média mensal
    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():
    # Exemplo de vetor de faturamento diário
    faturamento_diario = [
        5000, 6000, 0, 7000, 0, 8000, 10000, 9000, 0, 11000,
        12000, 0, 13000, 14000, 0, 15000, 16000, 17000, 0, 18000,
        0, 0, 19000, 20000, 0, 21000, 22000, 0, 23000, 24000
    ]
    
    menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)
    
    print(f"Menor valor de faturamento: R${menor:.2f}")
    print(f"Maior valor de faturamento: R${maior:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

if __name__ == "__main__":
    main()
