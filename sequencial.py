def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i  # Retorna o índice onde o alvo foi encontrado
    return -1  # Retorna -1 se o alvo não for encontrado

# Exemplo de uso
lista = [10, 23, 45, 70, 11, 15]
alvo = 70
resultado = busca_sequencial(lista, alvo)
print(f"Elemento encontrado no índice: {resultado}")
