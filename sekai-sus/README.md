# sus

Someone sent this file to me claiming he got it from a _SEKAI_ where the _palette_ is not _colorful_ but _purple_. I had no idea what he was talking about, only find it really _sus_.

Flag format (regex) `^SEKAI\{[\u0041-\u02AF]+\}$`

## Writeup
Hint suggest the game *Project SEKAI: Colorful Stage! feat. Hatsune Miku* and a custom chart server *Purple Palette*.
Reading the tutorial of the custom chart server, we see that `.sus` is the format to define such charts.

Google for _sus project sekai chart_ we can find this tool to draw the chart data out:
https://github.com/k0tayan/SekaiSUS2img

Draw the chart, and we can see the flag drawn letter by letter.