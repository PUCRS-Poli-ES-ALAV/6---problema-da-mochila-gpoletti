
instruction_count = 0
iteration_count = 0

instruction_count_rec = 0
iteration_count_rec = 0

def backpackPD(N, C, itens):
    global instruction_count, iteration_count
    instruction_count = 0
    iteration_count = 0

    maxTab = [[0 for _ in range(C + 1)] for _ in range(N + 1)]
    instruction_count += (N + 1) * (C + 1)

    for i in range(1, N + 1):
        for j in range(1, C + 1):
            instruction_count += 1
            iteration_count += 1

            if itens[i][0] <= j:
                instruction_count += 3
                maxTab[i][j] = max(maxTab[i - 1][j], itens[i][1] + maxTab[i - 1][j - itens[i][0]])
                instruction_count += 4
            else:
                maxTab[i][j] = maxTab[i - 1][j]
                instruction_count += 2

    instruction_count += 1
    return maxTab[N][C]

def backpack_recursive(N, C, itens):
    global instruction_count_rec, iteration_count_rec
    instruction_count_rec += 1

    if N == 0 or C == 0:
        instruction_count_rec += 1
        return 0

    instruction_count_rec += 1
    iteration_count_rec += 1

    if itens[N][0] > C:
        return backpack_recursive(N - 1, C, itens)

    else:
        include_item = itens[N][1] + backpack_recursive(N - 1, C - itens[N][0], itens)
        exclude_item = backpack_recursive(N - 1, C, itens)
        instruction_count_rec += 2
        return max(include_item, exclude_item)


def compare_algorithms():
    N = 10  # Número de itens
    C = 165  # Capacidade da mochila
    itens = [
        (0, 0),
        (23, 92), (31, 57), (29, 49), (44, 68), (53, 60),
        (38, 43), (63, 67), (85, 84), (89, 87), (82, 72)
    ]
    # N = 6  # Número de itens
    # C = 190  # Capacidade da mochila
    # itens = [
    #     (0, 0),
    #     (56, 50), (59, 50), (80, 64), (64, 46), (75, 50), (17, 5)
    # ]
    print("Running Backpack with Dynamic Programming...")
    result_dp = backpackPD(N, C, itens)
    dp_instructions = instruction_count
    dp_iterations = iteration_count

    print("Running Backpack with Recursion...")
    global instruction_count_rec, iteration_count_rec
    instruction_count_rec = 0
    iteration_count_rec = 0
    result_rec = backpack_recursive(N, C, itens)
    rec_instructions = instruction_count_rec
    rec_iterations = iteration_count_rec

    print("\nTabela de Comparação:")
    print(f"{'Algoritmo':<25} {'Resultado':<10} {'Instruções':<15} {'Iterações':<15}")
    print("-" * 65)
    print(f"{'Programação Dinâmica':<25} {result_dp:<10} {dp_instructions:<15} {dp_iterations:<15}")
    print(f"{'Recursivo (Divisão e Conquista)':<25} {result_rec:<10} {rec_instructions:<15} {rec_iterations:<15}")


# Executando a comparação
compare_algorithms()
