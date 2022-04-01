#!/usr/local/bin/python

import requests
import json
import random

def get_random(wiki):
    url = f"https://{wiki}.org/wiki/Special:Random"
    prefix = f"https://{wiki}.org/wiki/"
    return requests.get(url).url[len(prefix):]

def get_source(wiki, page):
    url = f"https://{wiki}.org/w/api.php?action=parse&page={page}&prop=text&formatversion=2&format=json"
    return requests.get(url).json()["parse"]["text"]


def is_found(source, dest):
    return f'<a href="/wiki/{dest}"' in source

try:
    weights_url = "https://commons.wikimedia.org/w/api.php?action=parse&page=Data:Wikipedia_statistics/data.tab&prop=wikitext&formatversion=2&format=json"
    weights_raw = json.loads(requests.get(weights_url).json()["parse"]["wikitext"])

    weights_pairs = [
        (i[0], i[3]) for i in weights_raw["data"]
        if i[0].endswith(".wikipedia") and not i[0].startswith("total")
    ]
    wikis = [i[0] for i in weights_pairs]
    weights = [i[1] for i in weights_pairs]

    wiki = random.choices(wikis, weights, k=1)[0]

    start = get_random(wiki)
    dest = get_random(wiki)
    prefix = f"https://{wiki}.org/wiki/"

    print("You have 10 tries to get to the destination.")
    print("You start at:", prefix + start)
    print("You want to get to:", prefix + dest)

    attempt = 1
    current = start
    current_source = get_source(wiki, start)
    reached = False

    while attempt <= 10:
        print()
        print(f"Attempt {attempt} / 10")
        print(f"Which link do you want to click from {prefix}{current}?")
        received = input(prefix)
        if not is_found(current_source, received):
            print(f"You cannot click {received}.")
        else:
            attempt += 1
            current = received
            if received == dest:
                reached = True
                break
            else:
                current_source = get_source(wiki, current)
    print()
    if reached:
        print("You made it!")
        with open("flag.txt") as f:
            print(f.read())
    else:
        print("Try harder next time!")
except Exception as e:
    print("Exception.")
