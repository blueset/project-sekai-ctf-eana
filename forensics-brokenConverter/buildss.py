from fontTools import ttLib

base = [chr(i) for i in range(33, 127)]
target = r"""f\@g:SEKAI{sCR4MBLeD_a5ci1-FONT+GlYPHZ,W3|!.d0n&}"#$%'()*/26789;<=>?JQUVX[]^`bhjkmopqrtuvwxyz~"""
assert set(base) == set(target) and len(base) == len(target)
rev_trans = dict(zip(target, base))

tt = ttLib.TTFont("scrambled.ttf")
cmap = {chr(int(k)): v for k, v in tt.getBestCmap().items()}

def build_ss(src, dst):
    chunk = []
    src_names = [cmap[i] for i in src]
    # src_names = [cmap[rev_trans[i]] for i in src]
    dst_names = [cmap[rev_trans[i]] for i in dst]
    for idx, i in enumerate(src_names):
        if idx < (len(src_names) - 1):
            print("sub", *(chunk), i + "'", *src_names[idx + 1:], "by", dst_names[idx], end="")
        else:
            print("sub", *(chunk), i + "'", *src_names[idx + 1:], "by", *dst_names[idx:], end="")
        print(";")
        chunk.append(dst_names[idx])

build_ss("flag", "SEKAI{OpenType")
print()
build_ss("flag", "MagicGSUB")
print()
build_ss("flag", "IsTuring")
print()
build_ss("flag", "Complete}")