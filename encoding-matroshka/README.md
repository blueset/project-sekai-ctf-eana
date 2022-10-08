# Layers
| Name | Target |
| ---- | ------ |
| Matroshka | (Starting point) |
| iPNG, Vaccination | `https://matryoshka.sekai.team/-qLf-Aoaur8ZVqK4aFngYg.png` |
| Noisy pair | `https://matryoshka.sekai.team/8d789414a7c58b5f587f8a050b8d788e.wav` |

# Flag

`SEKAI{KandoRyoko5Five2Two4Four}`

> 感度良好 524  
>       — マトリョシカ / ハチ


## Writeup (SEKAI ver.)


#### Stage 1

Screenshot shows that TCP 127.0.0.1:7943 encodes the input to a string of smiley faces of same length in different colors. Matching the sample input against the sample output, we can see that the same character would give the same set of colors.

The challenge statement hints about the 8 colors of ANSI Escape Sequences.

The colors are encoded in the following way:

```
M -(ASCII binary)-> 0 -(Foreground 0100)-> 0 -(Brightness)-> Dark
                    1                      1 -(Hue #4)-----> Blue
                    0                      0
                    0                      0
                    1 -(Foreground 1101)-> 1 -(Brightness)-> Bright
                    1                      1 -(Hue #5)-----> Magenta
                    0                      0
                    1                      1
```

The theme “Visual Studio Code Default Dark High Contrast“ indicates the palette to parse the colors from.

When decoded, the string shows `https://matryoshka.sekai.team/-qLf-Aoaur8ZVqK4aFngYg.png`.

#### Stage 2

The PNG file contains some noisy lines spreaded over the canvas. Opening it, several IDOT blocks can be found which hints it to be an Apple specific format.

Open the file with an Apple OS (iOS before 14 or macOS before 11 inclusive) to reveal the hidden image.

The bug in their PNG parsers has since been patched in later versions of Apple OSes.

Alternative solutions:
* Using browser testing platforms like [TestingBot](https://testingbot.com/) or [BrowserStack](https://www.browserstack.com/) to open the PNG in an earlier OS version. (discovered by sahuang)
* Use forensic tools like [FotoForensics](https://fotoforensics.com/) to decode the image mimicing Apple’s decoding method (discovered by [kaitoyama](https://trap.jp/post/1695/))
* Reverse [the script used to generate the PNG](https://github.com/DavidBuchanan314/ambiguous-png-packer/blob/main/pack.py) to get the encoded one. (discovered byy [remy_o](https://discord.com/channels/1004529434092654663/1004529435610972279/1026174670376030276))

<details>
  <summary>remy_o’s script</summary>
  
```py
import struct
import zlib

with open("Matryoshka-Step2.png", "rb") as f:
    data = f.read()

def decompress_headerless(data):
    d = zlib.decompressobj(wbits=-15)     
    result = d.decompress(data)     
    result += d.flush()     
 
    # do all the checks we can?
    assert(len(d.unconsumed_tail) == 0)     
    assert(len(d.unused_data) == 0)
 
    return result       

# Extract and concatenate IDAT chunks
w = open("matryoshka.out.png", "wb")
w.write(data[:8]) # header
c = data[8:]
idx = 1
idats = []
while c:
    length, = struct.unpack(">I", c[:4])
    typ = c[4:8]
    print("chunk", "length", length, "type", typ)
    if typ == b"IDAT":
        idats.append(c[8:8+length])
    else:
        # copy chunk
        if typ == b"IEND":
            # construct secret image
            idat1, idat2 = idats
            data1 = decompress_headerless(idat1[2:])
            data2 = decompress_headerless(idat2[:-4])
            idat_unpacked = data1 + data2
            # dump length32, IDAT, data, CRC
            idat = zlib.compress(idat_unpacked)
            w.write(len(idat).to_bytes(4, "big"))
            w.write(b"IDAT")
            w.write(idat)
            w.write(zlib.crc32(b"IDAT" + idat).to_bytes(4, "big"))
        w.write(c[:length+12])
    c = c[length+12:]
    idx += 1
print("parsed", idx-1, "chunks")
```

</details>

#### Stage 3

With hint on the picture “COVID-19 vaccination”, and the `shc:/` header of the text stored in the QR code. We can know that this is a https://smarthealth.cards/ card. Search for _SHC QR code decoder_ online, we find find plenty of tools to decode it.

Once decoded, the link to the next stage be found in the JSON payload: `https://matryoshka.sekai.team/8d789414a7c58b5f587f8a050b8d788e.wav`.

#### Stage 4

When the audio was played, a loud noise can be heard with some mild speech in the background. Opening the file with an audio editor, we can see that the file has 2 channels, with each channel has an almost opposite amplitude to the other. Split the channels into 2 mono files, and play them at the same time, the speech can be heard clearly.

> upper begin, sierra, echo, kilo, alfa, india, upper finish, open curly bracket, upper kilo, alfa, november, delta, oscar, upper romeo, yankee, oscar, kilo, oscar, five, upper foxtrot, india, victor, echo, two, upper tango, whiskey, oscar, fower, upper foxtrot, oscar, uniform, romeo, close curly bracket

The flag can be recovered from the NATO phonetic alphabet read in the audio.

Flag: `SEKAI{KandoRyoko5Five2Two4Four}`

### Trivia

The smiley face mark in Stage 1 was chosen as it made a significant appearance in [the music video of マトリョシカ by ハチ](https://www.youtube.com/watch?v=HOz-9FzIDf0).

> あなたと私でランデブー？  
>       — マトリョシカ / ハチ

> 感度良好 524  
>       — マトリョシカ / ハチ
