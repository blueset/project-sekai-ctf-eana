import sys
stdin = sys.stdin.buffer.read()
d = "".join(bin(i)[2:].zfill(8) for i in stdin)
p = ""
for i in range(0, len(d), 8):
    l = d[i:i+4]
    h = d[i+4:i+8]
    he = 40 if h[0] == "0" else 100
    he += int(h[1:], 2)
    le = 40 if l[0] == "0" else 100
    le += int(l[1:], 2)
    p += f"\033[{he}m☻\033[0m"
    p += f"\033[{le}m☻\033[0m"
    print(hex(int(l, 2))[2:], hex(int(h, 2))[2:])
print(p)
