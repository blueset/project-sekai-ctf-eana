# Sing it!
Well, it’s just too usual to hide a flag in stegano, database, cipher, or server. What if we decide to sing it out instead?

## Writeup

The source code suggest that the music file was generated based on the content of `flag.txt`, and choosing MP3 files from the downloaded JSON.

Thus, download the JSON and all MP3 files, then match each segment of 3 seconds against downloaded files to see which songs are included, then matching the ID of each song to get the flag.

Players can either match the tracks manually if they want to, or it is also possible to use tools like fpcalc for automation.

`SEKAI{v0CaloId<3u}`

> Vocaloid ❤️ U

## Credits

* [＊ハロー、プラネット。 / sasakure.UK](https://youtu.be/1gHHgx8bTxc)
* [ワールドイズマイン / ryo (supercell)](http://www.nicovideo.jp/watch/sm3504435)
* [自傷無色 / ねこぼーろ（ササノマリイ）](http://www.nicovideo.jp/watch/sm19870840)
* [霽れを待つ / Orangestar](https://youtu.be/wvlUWjqGQSA)
* [愛されなくても君がいる / ピノキオピー](https://youtu.be/ygY2qObZv24)
* [カトラリー / 有機酸](https://youtu.be/HHhFX9zUV2s)
* [ニア / 夏代孝明](http://www.nicovideo.jp/watch/sm31477166)
* [ECHO / Crusher](https://youtu.be/cQKGUgOfD8U)
* [悔やむと書いてミライ / まふまふ](https://youtu.be/jUyCN1229Ws)
* [セカイはまだ始まってすらいない / ピノキオピー](https://youtu.be/1s8NNPgdl5g)
* [ODDS & ENDS / ryo (supercell)](https://youtu.be/6OmwKZ9r07o)


## Footnote

Verified tools:
* https://github.com/kdave/audio-compare [PASSED]  
  Based on fpcalc, code change needed:
    ```py
    import glob
    from correlation import calculate_fingerprints, correlation
    segments = {i: calculate_fingerprints(i) for i in glob.glob("segments/*.mp3")}
    heads = {i: calculate_fingerprints(i) for i in glob.glob("heads/*.mp3")}
    for i, ico in segments.items():
      best = (0, None)
      for j, jco in heads.items():
          corr = correlation(ico, jco)
          if corr > best[0]:
              best = (corr, j)
      print(i, best[1])
    ```
* https://github.com/d4r3topk/comparing-audio-files-python [FAILED]  
  Broken code?
* https://pypi.org/project/compare-mp3/ [FAILED]  
  Library only compares **exact** same audio streams instead of similarity.
* https://pypi.org/project/audiodiff/ [FAILED]  
  Library only compares **exact** same audio streams instead of similarity.
* https://github.com/worldveil/dejavu [PASSED]  
  Based on numpy. Manual API invokes needed:
    ```py
    from dejavu import Dejavu
    from dejavu.logic.recognizer.file_recognizer import FileRecognizer
    from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer
    import glob

    config = { "database": { "host": "db", "user": "postgres", "password": "password", "database": "dejavu" }, "database_type": "postgres" }

    djv = Dejavu(config)

    djv.fingerprint_directory("heads", [".mp3"])
    for i in glob.glob("segments/*.mp3"):
        print(i, djv.recognize(FileRecognizer, i)["results"][0]["song_name"])
    ```
