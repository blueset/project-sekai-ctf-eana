import json
import requests
import os
from collections import defaultdict
import dateutil.parser as dp

def iso8601_to_unix_timestamp(iso8601):
    return int(dp.parse(iso8601).timestamp())

cookie = os.environ.get("COOKIE", "")
path = os.environ.get("API_PATH", "https://ctf.sekai.team/api/v1/")

challs = requests.get(path + "challenges", cookies={"session": cookie}).json()["data"]
id_names = {i["id"]: i["name"] for i in challs}

result = {
    "tasks": list(id_names.values()),
    "standings": []
}

team_solve = defaultdict(lambda: {"taskStats": {}})

for chall in challs:
    cid = chall["id"]
    cname = chall["name"]
    cpoints = chall["value"]
    solves = requests.get(path + f"challenges/{cid}/solves", cookies={"session": cookie}).json()["data"]
    for s in solves:
        tid = s["account_id"]
        team_solve[tid]["taskStats"][cname] = { "points": cpoints, "time": iso8601_to_unix_timestamp(s["date"]) }

scoreboard = requests.get(path + "scoreboard", cookies={"session": cookie}).json()["data"]
for team in scoreboard:
    solves = team_solve[team["account_id"]]["taskStats"]
    obj = {
        "pos": team["pos"],
        "team": team["name"],
        "score": team["score"],
        "taskStats": solves,
        "lastAccept": max(ts["time"] for ts in solves.values()) if solves else None
    }
    result["standings"].append(obj)

print(json.dumps(result, indent=4))