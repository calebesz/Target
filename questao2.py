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
