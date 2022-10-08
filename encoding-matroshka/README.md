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
