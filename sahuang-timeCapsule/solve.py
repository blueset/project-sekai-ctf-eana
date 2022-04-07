import random
from itertools import permutations

def shuffle(message, key):
    res = []
    for i in key:
        for j in range(i, len(message), len(key)):
            res.append(message[j])

    return res

encoded = open("flag.enc", "rb").read()
now = bytes(i^0x42 for i in encoded[-18:])
flag = encoded[:-18]

random.seed(now)
key2 = [random.randrange(256) for _ in flag]

flag2 = bytes([m ^ k for (m,k) in zip(flag, key2)])

for i in permutations(range(8), 8):
    order = list(range(len(flag2)))
    for _ in range(42):
        order = shuffle(order, list(i))
    flag1 = [None] * len(flag2)
    for jdx, j in zip(order, flag2):
        flag1[jdx] = j
    flag1 = bytes(flag1)
    if flag1.startswith(b"SEKAI{"):
        print(flag1)
