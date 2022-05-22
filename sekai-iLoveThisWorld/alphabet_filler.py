import json

phonemes = """k ow l ax n
ow p ax n k er l iy b r ae k ih t
k l ow s k er l iy b r ae k ih t
ey
b iy
s iy
d iy
iy
eh f
jh iy
ey ch
ay
jh ey
k ey
eh l
eh m
eh n
ow
p iy
k y uw
aa r
eh s
t iy
y uw
v iy
d ah b ax l y uw
eh k s
w ay
z iy
w ah n
t uw""".splitlines()
letters = ":{}ABCDEFGHIJKLMNOPQRSTUVWXYZ12"
alphabet = dict(zip(letters, phonemes))

flag = "FLAG:SEKAI{SM1ZFARAWAYTMRISTHESEQUEL2OURDREAMTDY}"

jdata = open("ilovethisworld.svp","rb").read()[:-1].decode()
data = json.loads(jdata)
for idx, note in enumerate(data["library"][0]["notes"]):
    note["phonemes"] = alphabet[flag[idx]]

with open("ilovethisworld_p.svp", "w") as f:
    json.dump(data, f)
    f.write("\0")
