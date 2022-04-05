"""Solve script for sahuang’s Matrix Lab 1.
decrypt, get_array, and transform are directly translated from the
decompiled source.
decrypt, put_matrix, and recover are the reverse process of the 
methods.
"""

def encrypt(seq, key):
    ans = ["�"] * 12
    l = 6
    r = l - 1
    for i in range(0, 12, 2):
        ans[i] = seq[l]
        l -= 1
        ans[i + 1] = seq[r]
        r += 1

    for i in range(0, 12):
        ans[i] = chr(ord(ans[i]) ^ key)
    
    return "".join(ans)

def decrypt(ans, key):
    ans = list(chr(ord(i) ^ key) for i in ans)
    seq = ["�"] * 12
    l = 5
    r = 6
    for i in range(0, 12, 2):
        seq[l] = ans[i]
        l -= 1
        seq[r] = ans[i + 1]
        r += 1
    return seq

def get_array(matrix, x, y):
    ans = ["�"] * 12
    ptr = 0
    for i in range(6):
        ans[ptr] = matrix[x][i]
        ptr += 1
    for i in range(6):
        ans[ptr] = matrix[y][5 - i]
        ptr += 1
    return ans

def put_matrix(ans, matrix, x, y):
    matrix[x] = ans[:6]
    matrix[y] = ans[-1:5:-1]

def transform(seq):
    matrix = [["�"] * 6 for _ in range(6)]
    for i in range(36):
        x = i // 6
        y = i % 6
        matrix[x][y] = seq[i]
    return matrix

def recover(matrix):
    return "".join(sum(matrix, []))

cipher = "oz]{R]3l]]B#50es6O4tL23Etr3c10_F4TD2"
group1 = cipher[:12]
group2 = cipher[12:24]
group3 = cipher[24:]

dgroup1 = decrypt(group1, 2)
dgroup2 = decrypt(group2, 1)
dgroup3 = decrypt(group3, 0)

matrix = [["�"] * 6 for _ in range(6)]
put_matrix(dgroup1, matrix, 0, 5)
put_matrix(dgroup2, matrix, 1, 4)
put_matrix(dgroup3, matrix, 2, 3)

for i in range(4):
    for j in range(5 - 2*i):
        # (
        #     matrix[i][i + j],
        #     matrix[5 - i - j][i],
        #     matrix[5 - i][5 - i - j],
        #     matrix[i + j][5 - i],
        # ) = (
        #     matrix[5 - i - j][i],
        #     matrix[5 - i][5 - i - j],
        #     matrix[i + j][5 - i],
        #     matrix[i][i + j],
        # )
        (
            matrix[5 - i - j][i],
            matrix[5 - i][5 - i - j],
            matrix[i + j][5 - i],
            matrix[i][i + j],
        ) = (
            matrix[i][i + j],
            matrix[5 - i - j][i],
            matrix[5 - i][5 - i - j],
            matrix[i + j][5 - i],
        )

print(recover(matrix))
