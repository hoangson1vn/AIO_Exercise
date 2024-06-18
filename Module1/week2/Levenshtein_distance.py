def levenshtein_distance(token1, token2):
    a, b = len(token1), len(token2)

    # create matrix_sample size (m+1) x (n+1)
    matrix_sample = [[0] * (b + 1) for _ in range(a + 1)]

    for i in range(a + 1):
        matrix_sample[i][0] = i
    for j in range(b + 1):
        matrix_sample[0][j] = j

    # fill matrix matrix_sample
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if token1[i - 1] == token2[j - 1]:
                matrix_sample[i][j] = matrix_sample[i - 1][j - 1]
            else:
                matrix_sample[i][j] = min(
                    matrix_sample[i - 1][j] + 1,
                    matrix_sample[i][j - 1] + 1,
                    matrix_sample[i - 1][j - 1] + 1
                )

    return matrix_sample[a][b]


print(levenshtein_distance("Hello", "ello"))
print(levenshtein_distance("flaw", "lawn"))
