curl https://sekai-world.github.io/sekai-master-db-diff/musicVocals.json | jq -r '.[]|select( .musicId > 32 and .musicId < 128)|.assetbundleName|"https://storage.sekai.best/sekai-assets/music/short/\(.)_rip/\(.)_short.mp3"' | wget -i - -P ./source
for i in source/*.mp3; do ffmpeg -i "$i" -t 3 "heads/${i##*/}"; done
ffmpeg -i flag.mp3 -map 0 -segment_time 00:00:03 -f segment segments/%03d.mp3
