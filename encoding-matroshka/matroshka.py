import sys
text = sys.stdin.read()

# for i in list(range(30, 38)):
#     for j in list(range(40, 48)):
#         print(f"\033[{i};{j}m☻\033[0m", end="")
#         print(f"\033[{i};{j+60}m☻\033[0m", end="")
#     print()
#     for j in list(range(40, 48)):
#         print(f"\033[{i+60};{j}m☻\033[0m", end="")
#         print(f"\033[{i+60};{j+60}m☻\033[0m", end="")
#     print()

bits = "".join(bin(ord(i))[2:].zfill(8) for i in text)
bits = bits.ljust(len(bits) + (10 - (len(bits) % 10)) % 10, "0")

result = ""
for i in range(0, len(bits), 10):
    left = bits[i:i+5]
    right = bits[i+5:i+10]
    # print(left, right)
    lcolor = 30 if left[0] == "0" else 90
    lcolor += int(left[1:], 2)
    rcolor = 40 if right[0] == "0" else 100
    rcolor += int(right[1:], 2)
    result += f"\033[{lcolor};{rcolor}m☻\033[0m"

print(result)
