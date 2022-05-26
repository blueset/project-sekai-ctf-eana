import numpy

flag = "SEKAI{"

matrix = numpy.array([
    [2094, 2962, 1014, 2102], 
    [2172, 3955, 1174, 3266], 
    [3186, 4188, 1462, 3936], 
    [3583, 5995, 1859, 5150]]
)
# X = magic(4)
X = numpy.array([
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 6, 12],
    [4, 14, 15, 1],
])
# Y = pascal(4)
Y = numpy.array([
    [1, 1, 1, 1],
    [1, 2, 3, 4],
    [1, 3, 6, 10],
    [1, 4, 10, 20],
])

C = X + Y

# C * Btr901337 = matrix
# Btr901337 = C′ * B
Btr901337 = numpy.matmul(numpy.linalg.inv(C), matrix)
Bt = numpy.rot90(Btr901337, -1337)
B = numpy.transpose(Bt)
A = B.flatten()
# Round to nearest int
A = numpy.rint(A).astype(int)
flag += "".join(chr(i ^ 42) for i in A)

flag += "}"

print(flag)
