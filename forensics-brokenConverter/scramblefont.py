from fontTools import ttLib

base = [chr(i) for i in range(33, 127)]
target = r"""f\@g:SEKAI{sCR4MBLeD_a5ci1-FONT+GlYPHZ,W3|!.d0n&}"#$%'()*/26789;<=>?JQUVX[]^`bhjkmopqrtuvwxyz~"""
assert set(base) == set(target) and len(base) == len(target)
trans = dict(zip(base, target))
rev_trans = dict(zip(target, base))

tt = ttLib.TTFont("CascadiaCode.subset.ttf")


cmap = {chr(int(k)): v for k, v in tt.getBestCmap().items()}
cmap_names_in_range = set(cmap[i] for i in base)

assert all(i in cmap for i in base)

new_glyf = {}

for i in base:
    new_glyf[cmap[i]] = tt["glyf"][cmap[trans[i]]]

for i in tt["glyf"].keys():
    if i not in cmap_names_in_range:
        new_glyf[i] = tt["glyf"][i]
for i in new_glyf:
    tt["glyf"][i] = new_glyf[i]

double_quote_name = cmap[rev_trans['"']]
single_quote_name = cmap[rev_trans["'"]]
double_quote = tt["glyf"][double_quote_name]
double_quote.components[0].glyphName = single_quote_name
double_quote.components[1].glyphName = single_quote_name
new_hmtx = {}

for i in base:
    new_hmtx[cmap[i]] = tt["hmtx"][cmap[trans[i]]]

cmap_names_in_range = set(cmap[i] for i in base)

for i in tt["hmtx"].metrics.keys():
    if i not in cmap_names_in_range:
        new_hmtx[i] = tt["hmtx"][i]
for i in new_hmtx:
    tt["hmtx"][i] = new_hmtx[i]

tt.save("scrambled.ttf")

