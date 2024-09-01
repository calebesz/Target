def inverter_string(s):
    # Converte a string em uma lista de caracteres
    lista_caracteres = list(s)
    # Inicializa variáveis para as posições inicial e final
    inicio = 0
    fim = len(lista_caracteres) - 1
    
    # Inverte a lista de caracteres
    while inicio < fim:
        # Troca os caracteres nas posições inicio e fim
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        # Move as posições
        inicio += 1
        fim -= 1
    
    # Converte a lista de volta para uma string
    return ''.join(lista_caracteres)

def main():
    # Solicita ao usuário para informar a string ou define uma string previamente
    string_original = input("Digite uma string para inverter (ou pressione Enter para usar a string padrão): ")
    
    if not string_original:
        string_original = "Exemplo de string para inverter"
    
    string_invertida = inverter_string(string_original)
    
    print(f"String original: {string_original}")
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
