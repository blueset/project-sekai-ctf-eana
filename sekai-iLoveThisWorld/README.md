# I love this world (Lite)

Vocaloid is a great software to get you computer sing the flag out to you, but what if you can’t afford it?
No worries, there are plenty of other free tools you can use. How about — let’s say — this one?

Flag format (Regex): `SEKAI\{[A-Z0-9]+\}`

## Writeup
As hinted in the question statement, the flag is sang out in the file. The file is a project file of [Synthesizer V], which is a cross-platform singing synthesizer software that comes with a free version. Opening the file, it shows a JSON file that shows all the configurations of the track.

Inspecting the lyrics, we can see this line below, which is obviously not the flag as it does not match the flag format.

> きみをおもうひとのかずだけ, きみをつくるみらいがある, きみをはくぐむよーなこのSEKAI{が, ぼくわすきなんだ}

Looking further into each note, we can see all of them are definded with a specific set of phonemes:

> eh f, eh l, ey, jh iy, k ow l ax n, eh s, iy, k ey, ey, ay, ow p ax n k er l iy b r ae k ih t, eh s, eh m, w ah n, z iy, eh f, ey, aa r, ey, d ah b ax l y uw, ey, w ay, t iy, eh m, aa r, ay, eh s, t iy, ey ch, iy, eh s, iy, k y uw, y uw, iy, eh l, t uw, ow, y uw, aa r, d iy, aa r, iy, ey, eh m, t iy, d iy, w ay, k l ow s k er l iy b r ae k ih t

Looking further down the JSON file, we can see that Synthesizer V is using [ARPABET] as the phoneme standard. Reading out the entire lyrics using ARPABET, we can get:

> F, L, A, G, colon, S, E, K, A, I, open curly bracket, S, M, one, Z, F, A, R, A, W, A, Y, T, M, R, I, S, T, H, E, S, E, Q, U, E, L, two, O, U, R, D, R, E, A, M, T, D, Y, close curly braket

...which gives you the flag.

Flag: `SEKAI{SM1ZFARAWAYTMRISTHESEQUEL2OURDREAMTDY}`

> Someone’s faraway tomorrow is the sequel to our dream today.

[Synthesizer V]: https://dreamtonics.com/en/synthesizerv/
[ARPABET]: https://en.wikipedia.org/wiki/ARPABET

# I love this world

**D**id **y**ou k**n**ow?  
Vo**c**a**l**oid is a voic**e** synthesizer software developed by Yamaha.  
Cy**b**e**r** D**i**va and Cyber Songman are the first two first-party English-only voicebanks of Vocaloid.

Flag format (Regex): `SEKAI\{[A-Z]+\}`

## Writeup
Hint suggest looking at DYN, CLE, and BRI parameter of the VSQX file.

Overlapping the parameters, we can see the flag.

![Flag preview](./Params.png)

(Blue: DYN, Green: CLE, Red: BRI)

Flag: `SEKAI{SMONEZTMRISOURDREAMTDY}`

> Someone’s tomorrow is our dream today.

> キミを想う人の数だけ  
> キミを創る未来がある  
> キミを育むようなこの世界が  
> 僕は好きなんだ
> 
> どこかの誰かの遠い明日は  
> 今日の僕らの夢の続き
>
> — [I Love This World / にとぱん](https://www.nicovideo.jp/watch/sm23073336)