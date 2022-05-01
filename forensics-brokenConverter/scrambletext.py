from bs4 import BeautifulSoup as bs

with open("1.fpage", "rb") as f:
    soup = bs(f.read(), "xml")

base = [chr(i) for i in range(33, 127)]
target = r"""f\@g:SEKAI{sCR4MBLeD_a5ci1-FONT+GlYPHZ,W3|!.d0n&}"#$%'()*/26789;<=>?JQUVX[]^`bhjkmopqrtuvwxyz~"""
assert set(base) == set(target) and len(base) == len(target)
trans = dict(zip(target, base))

for g in soup.find_all("Glyphs"):
    txt = g.attrs["UnicodeString"]
    txt = "".join(trans.get(i, i) for i in txt)
    g.attrs["UnicodeString"] = txt

# write xml content
with open("lipsum/Documents/1/Pages/1.fpage", "w") as f:
    f.write(soup.prettify())
