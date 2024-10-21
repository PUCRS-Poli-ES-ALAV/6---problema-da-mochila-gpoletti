import sys

# Definindo limites para a recursão
sys.setrecursionlimit(100000)

# Contadores globais
instruction_count_rec = 0
instruction_count_iter = 0
instruction_count_memo = 0

iteration_count_rec = 0
iteration_count_iter = 0
iteration_count_memo = 0

# Estrutura para armazenar os resultados
results = {
    "Recursive": [],
    "Iterative": [],
    "Memoized": []
}


def fibo_rec(n):
    global instruction_count_rec, iteration_count_rec
    instruction_count_rec += 1  # Contabiliza instruções
    if n <= 1:
        return n
    iteration_count_rec += 1  # Contabiliza iterações
    return fibo_rec(n - 1) + fibo_rec(n - 2)


def fibo_iter(n):
    global instruction_count_iter, iteration_count_iter
    instruction_count_iter += 1  # Início do algoritmo
    if n <= 1:
        return n

    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    instruction_count_iter += 4  # Instruções de inicialização
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        instruction_count_iter += 3  # Instruções no loop
        iteration_count_iter += 1  # Contabiliza iterações
    return f[n]


def memoized_fibo(f, n):
    global instruction_count_memo, iteration_count_memo
    instruction_count_memo += 1  # Contabiliza instruções
    if f[n] != -1:
        return f[n]
    if n <= 1:
        f[n] = n
    else:
        iteration_count_memo += 1  # Contabiliza iterações
        f[n] = memoized_fibo(f, n - 1) + memoized_fibo(f, n - 2)
    return f[n]


def store_results(algorithm, n, result, instructions, iterations):
    results[algorithm].append({
        "n": n,
        "result": result,
        "instructions": instructions,
        "iterations": iterations
    })


def run_tests():
    test_values = [4, 8, 16, 32, 128, 1000, 10000]

    # Fibonacci Recursive
    print("Running Fibonacci Recursive...")
    for n in test_values:
        if n <= 32:  # Limitar o FiboRec a um tamanho de entrada razoável
            global instruction_count_rec, iteration_count_rec
            instruction_count_rec = 0
            iteration_count_rec = 0
            result = fibo_rec(n)
            store_results("Recursive", n, result, instruction_count_rec, iteration_count_rec)

    # Fibonacci Iterative
    print("Running Fibonacci Iterative...")
    for n in test_values:
        global instruction_count_iter, iteration_count_iter
        instruction_count_iter = 0
        iteration_count_iter = 0
        result = fibo_iter(n)
        store_results("Iterative", n, result, instruction_count_iter, iteration_count_iter)

    # Fibonacci Memoized
    print("Running Fibonacci Memoized...")
    for n in test_values:
        global instruction_count_memo, iteration_count_memo
        instruction_count_memo = 0
        iteration_count_memo = 0
        memo = [-1] * (n + 1)
        result = memoized_fibo(memo, n)
        store_results("Memoized", n, result, instruction_count_memo, iteration_count_memo)


def print_results_table():
    print(f"{'Algorithm':<12} {'n':<6} {'Instructions':<12} {'Iterations':<12}")
    print("-" * 60)

    for algo in results:
        for entry in results[algo]:
            print(
                f"{algo:<12} {entry['n']:<6} {entry['instructions']:<12} {entry['iterations']:<12}")


if __name__ == "__main__":
    run_tests()
    print_results_table()
