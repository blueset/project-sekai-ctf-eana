import requests
import random
import subprocess

tracks = requests.get("https://sekai-world.github.io/sekai-master-db-diff/musics.json").json()
resources = requests.get("https://sekai-world.github.io/sekai-master-db-diff/musicVocals.json").json()

def pick(char):
    return random.choice([i["id"] for i in tracks if i["title"].startswith(char)])

def get_resource(mid):
    return sorted([i for i in resources if i["musicId"] == mid], key=lambda a: a["caption"])[-1]["assetbundleName"]

def download(mid):
    resource = get_resource(mid)
    r = requests.get(f"https://sekai-res.dnaroma.eu/file/sekai-assets/music/short/{resource}_rip/{resource}_short.mp3")
    print(resource)
    filename = f"tracks/{mid}.mp3"
    with open(filename, "wb") as f:
        f.write(r.content)
    return mid

with open("flag.txt") as f:
    flag = f.read().strip()

tracks = [download(pick(i)) for i in flag]

inputs = sum([["-i", f"tracks/{i}.mp3"] for i in tracks], [])
filters = "".join(f"[{i}:a]atrim=end=1,asetpts=PTS-STARTPTS[a{i}];" for i in range(len(tracks))) + \
          "".join(f"[a{i}]" for i in range(len(tracks))) + \
          f"concat=n={len(tracks)}:v=0:a=1[a]"

subprocess.run(["ffmpeg"] + inputs + ["-filter_complex", filters, "-map", "[a]", "flag.mp3"])
