def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    passos = 0  # Variável para contar o número de passos

    while inicio <= fim:
        passos += 1  # Incrementa o contador de passos a cada iteração
        meio = (inicio + fim) // 2

        # Verifica se o alvo está no meio
        if lista[meio] == alvo:
            return meio, passos  # Retorna o índice e o número de passos
        # Se o alvo for menor, desconsidera a metade superior
        elif lista[meio] > alvo:
            fim = meio - 1
        # Se o alvo for maior, desconsidera a metade inferior
        else:
            inicio = meio + 1

    return -1, passos  # Retorna -1 se o alvo não for encontrado, e o número de passos


# Exemplo de uso
lista = [10, 23, 45, 50, 70, 80, 100, 120]
alvo = 50
resultado, passos = busca_binaria(lista, alvo)
print(f"Elemento encontrado no índice: {resultado}, em {passos} passo(s).")
