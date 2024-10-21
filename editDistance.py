instruction_count_rec_ed = 0
iteration_count_rec_ed = 0
instruction_count_dp_ed = 0
iteration_count_dp_ed = 0

def edit_distance_recursive(S, T, i, j):
    global instruction_count_rec_ed, iteration_count_rec_ed
    instruction_count_rec_ed += 1

    if i == 0:
        return j
    if j == 0:
        return i

    iteration_count_rec_ed += 1

    if S[i - 1] == T[j - 1]:
        return edit_distance_recursive(S, T, i - 1, j - 1)

    return 1 + min(
        edit_distance_recursive(S, T, i - 1, j - 1),
        edit_distance_recursive(S, T, i, j - 1),
        edit_distance_recursive(S, T, i - 1, j)
    )


def edit_distance_dp(S, T):
    global instruction_count_dp_ed, iteration_count_dp_ed
    m = len(S)
    n = len(T)

    matriz = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        matriz[i][0] = i
        instruction_count_dp_ed += 1
        iteration_count_dp_ed += 1

    for j in range(1, n + 1):
        matriz[0][j] = j
        instruction_count_dp_ed += 1
        iteration_count_dp_ed += 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                custoExtra = 0
            else:
                custoExtra = 1
            matriz[i][j] = min(
                matriz[i - 1][j] + 1,
                matriz[i][j - 1] + 1,
                matriz[i - 1][j - 1] + custoExtra
            )
            instruction_count_dp_ed += 3
            iteration_count_dp_ed += 1

    return matriz[m][n]


def compare_edit_distance():
    s1_case1 = "Casablanca"
    s2_case1 = "Portentoso"
    s1_case2 = ("Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to " +
                "simplify the build processes in the Jakarta Turbine project. There were several " +
                "projects, each with their own Ant build files, that were all slightly different. " +
                "JARs were checked into CVS. We wanted a standard way to build the projects, a clear " +
                "definition of what the project consisted of, an easy way to publish project information " +
                "and a way to share JARs across several projects. The result is a tool that can now be " +
                "used for building and managing any Java-based project. We hope that we have created " +
                "something that will make the day-to-day work of Java developers easier and generally help " +
                "with the comprehension of any Java-based project.")

    s2_case2 = ("This post is not about deep learning. But it could be might as well. This is the power of " +
                "kernels. They are universally applicable in any machine learning algorithm. Why you might " +
                "ask? I am going to try to answer this question in this article. " +
                "Go to the profile of Marin Vlastelica Pogančić " +
                "Marin Vlastelica Pogančić Jun")

    global instruction_count_rec_ed, iteration_count_rec_ed, instruction_count_dp_ed, iteration_count_dp_ed

    # Caso 1: s1 = "Casablanca", s2 = "Portentoso"
    instruction_count_rec_ed = 0
    iteration_count_rec_ed = 0
    result_rec_case1 = edit_distance_recursive(s1_case1, s2_case1, len(s1_case1), len(s2_case1))

    instruction_count_dp_ed = 0
    iteration_count_dp_ed = 0
    result_dp_case1 = edit_distance_dp(s1_case1, s2_case1)

    # Print the table of comparison
    print("\nTabela de Comparação:")
    print(f"{'Caso':<10} {'Algoritmo':<35} {'Resultado':<10} {'Instruções':<15} {'Iterações':<15}")
    print("-" * 85)
    print(
        f"{'Caso 1':<10} {'Recursivo (Divisão e Conquista)':<35} {result_rec_case1:<10} {instruction_count_rec_ed:<15} {iteration_count_rec_ed:<15}")
    print(
        f"{'Caso 1':<10} {'Programação Dinâmica':<35} {result_dp_case1:<10} {instruction_count_dp_ed:<15} {iteration_count_dp_ed:<15}")

    # Caso 2: s1 = "Maven, a Yiddish...", s2 = "This post is not..."
    instruction_count_rec_ed = 0
    iteration_count_rec_ed = 0
    result_rec_case2 = 0#edit_distance_recursive(s1_case2, s2_case2, len(s1_case2), len(s2_case2))

    instruction_count_dp_ed = 0
    iteration_count_dp_ed = 0
    result_dp_case2 = edit_distance_dp(s1_case2, s2_case2)


    print(
        f"{'Caso 2':<10} {'Recursivo (Divisão e Conquista)':<35} {result_rec_case2:<10} {instruction_count_rec_ed:<15} {iteration_count_rec_ed:<15}")
    print(
        f"{'Caso 2':<10} {'Programação Dinâmica':<35} {result_dp_case2:<10} {instruction_count_dp_ed:<15} {iteration_count_dp_ed:<15}")


compare_edit_distance()


