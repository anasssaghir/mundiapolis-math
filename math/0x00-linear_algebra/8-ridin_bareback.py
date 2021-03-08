def mat_mul(mat1, mat2):
    lines1, lines2 = len(mat1), len(mat2)
    rows1, rows2 = len(mat1[0]), len(mat2[0])

    if lines2 != rows1:
        return None
    else:
        new = [[0 for i in range(rows2)] for j in range(lines1)]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    new[i][j] += mat1[i][k] * mat2[k][j]
        return new