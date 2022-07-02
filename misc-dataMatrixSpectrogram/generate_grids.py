#%%
from pylibdmtx.pylibdmtx import encode
from PIL import Image, ImageOps
encoded = encode(b'vsctf{<><>Stop&-&^&TalkBBABStart}')
img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
# %%
img1 = Image.new('RGB', (encoded.width, encoded.height), (255, 255, 255))
img2 = Image.new('RGB', (encoded.width, encoded.height), (255, 255, 255))
for i in range(0, img.size[0], 5):
    for j in range(0, img.size[1], 5):
        target = img1 if (i + j) % 2 else img2
        region = (i, j, i + 5, j + 5)
        crop = img.crop(region)
        target.paste(crop, region)

# %%
ImageOps.invert(img1).save("L.png")
ImageOps.invert(img2).save("R.png")
# %%
