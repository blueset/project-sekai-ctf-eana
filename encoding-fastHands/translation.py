import json
from collections import defaultdict

data = json.loads(open("main.json").read())
rdata = defaultdict(set)
for k, v in data.items():
    rdata[v].add(k)

chord = "STKPWHRAO*EUFRPBLGTSDZ"
"       |  K W R   E F  B G    $"

def format(key):
    placements = key.split("/")
    ans = []
    for p in placements:
        p = list(p)
        c = []
        for key in chord:
            if p and p[0] == "-" and key == "*":
                c.append(" ")
                p.pop(0)
            elif p and p[0] == key:
                c.append(key)
                p.pop(0)
            else:
                c.append(" ")
        ans.append("".join(c) + "$")
    return ans

def generate(words):
    count = []
    for w in words:
        if w in rdata:
            rd = sorted(rdata[w], key=lambda x: len(x))[0]
            ans = format(rd)
            print(*ans, sep="\n")
            count.append(len(ans))
        else:
            print("???")
            count.append("-1")
    for w, c in zip(words, count):
        print(w, c)

if __name__ == "__main__":
    generate("""the
word
can
with
capitalized
{&N}
followed
by
an
underscore""".splitlines())
