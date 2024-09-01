# Target

## 1. Cálculo da Soma dos Números de 1 a INDICE

Dado o seguinte trecho de código:

```cpp
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
```
Resultado: 91
## 2. Verificação de Pertencimento à Sequência de Fibonacci

Dado o seguinte problema:

Verifique se um número informado pertence à sequência de Fibonacci.

```python
def pertence_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    
    return a == n

def main():
    try:
        numero = int(input("Digite um número: "))
        if pertence_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
```

## 3. Cálculo do Menor e Maior Faturamento e Dias Acima da Média

Dado o seguinte problema:

Calcule o menor e maior valor de faturamento ocorrido em um dia do mês e o número de dias em que o valor de faturamento diário foi superior à média mensal. Ignore os dias sem faturamento.

```python
def calcular_faturamento(faturamento_diario):
    dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
    
    if not dias_com_faturamento:
        return "Nenhum faturamento registrado no mês."
    
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():
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

```

## 4. Percentual de Representação por Estado

Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros – R$19.849,53

Calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

```python
def calcular_percentuais(faturamento_por_estado):
    total_faturamento = sum(faturamento_por_estado.values())
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_por_estado.items()}
    return percentuais

def main():
    faturamento_por_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    percentuais = calcular_percentuais(faturamento_por_estado)
    
    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
```

## 5. Inversão de Caracteres de uma String

Escreva um programa que inverta os caracteres de uma string.

```python
def inverter_string(s):
    lista_caracteres = list(s)
    inicio = 0
    fim = len(lista_caracteres) - 1
    
    while inicio < fim:
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        inicio += 1
        fim -= 1
    
    return ''.join(lista_caracteres)

def main():
    string_original = input("Digite uma string para inverter (ou pressione Enter para usar a string padrão): ")
    
    if not string_original:
        string_original = "Exemplo de string para inverter"
    
    string_invertida = inverter_string(string_original)
    
    print(f"String original: {string_original}")
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
```
