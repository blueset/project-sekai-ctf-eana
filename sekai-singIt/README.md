# Sing it!
Well, it’s just too usual to hide a flag in stegano, database, cipher, or server. What if we decide to sing it out instead?

## Writeup

The source code suggest that the music file was generated based on the `flag.txt`, and choosing MP3 files from the downloaded JSON.

Thus, download the JSON and all MP3 files, then match each second of it against files to see which songs are included, then pick out the first character of each song’s name as the flag.

`SEKaエ「ボオカロいドウタおう＊`