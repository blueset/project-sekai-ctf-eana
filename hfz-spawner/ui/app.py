#!/usr/bin/python3
from flask import Flask, jsonify, render_template, session, request
import json
import random

app = Flask(__name__, static_folder="vite/dist/assets")
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

CHALLENGES = [
    {
        "id": 0,
        "name": "Scanner Service",
        "category": "Web",
        "hidden": False,
        "proto": "http",
        "lifetime": 300,
    },
    {
        "id": 1,
        "name": "Hibana",
        "category": "Pwn",
        "hidden": False,
        "proto": "udp",
        "lifetime": 300,
    },
]
INSTANCES = [
    {
        "team_id": 0,
        "challenge_id": 0,
        "host": "127.0.0.1",
        "port": 1337,
        "password": "SEKAI",
    }
]


@app.route("/", methods=["GET"])
def root():
    if app.testing or app.debug:
        headers = """
        <script type="module">
            import RefreshRuntime from 'http://localhost:5173/@react-refresh'
            RefreshRuntime.injectIntoGlobalHook(window)
            window.$RefreshReg$ = () => {}
            window.$RefreshSig$ = () => (type) => type
            window.__vite_plugin_react_preamble_installed__ = true
        </script>
        <script type="module" src="http://localhost:5173/@vite/client" onerror="alert('launch vite dev with `npm run dev` in `vite` directory.')"></script>
        <script type="module" src="http://localhost:5173/src/main.tsx"></script>
        """
    else:
        headers = ""
        with open("./vite/dist/manifest.json") as f:
            manifest = json.load(f)
            resources = next(i for i in manifest.values() if i.get("isEntry"))
            headers = "".join(
                f'<link rel="stylesheet" href="{ css }" />' for css in resources["css"]
            ) + f'<script type="module" src="{ resources["file"] }"></script>'

    return render_template("index.html", headers=headers)

@app.route("/challenges", methods=["GET"])
def challenges():
    counter = (session.get("counter", 0) + 1) % 5
    chals = []
    challenge_dict = {challenge["id"]: challenge for challenge in CHALLENGES}
    instances = INSTANCES.copy()
    if counter == 0:
        instances.append(
            {
                "team_id": 0,
                "challenge_id": 1,
                "host": "127.0.0.1",
                "port": counter,
                "password": "Passworrrrrrr",
            }
        )
    print(session.get("counter", "no counter"), counter, instances)
    for instance in instances:
        challenge = challenge_dict[instance["challenge_id"]].copy()
        challenge["running"] = True
        challenge["host"] = instance["host"]
        challenge["port"] = instance["port"]
        challenge["password"] = instance["password"]
        challenge["remaining"] = random.randint(150, 300)
        chals.append(challenge)
        del challenge_dict[instance["challenge_id"]]
    chals += [*challenge_dict.values()]
    session["counter"] = counter

    return jsonify(success=True, challenges=chals)

@app.route("/launcher", methods=["POST"])
def launch():
    challenge_id = request.json.get("challenge_id")
    if challenge_id is None:
        return jsonify(success=False, msg="Missing challenge ID.")

    if isinstance(challenge_id, str) and not challenge_id.isdigit():
        return jsonify(success=False, msg="Challenge ID must be numeric.")

    challenge_id = int(challenge_id)
    if challenge_id not in range(len(CHALLENGES)):
        return jsonify(success=False, msg="No such challenge.")

    challenge = CHALLENGES[challenge_id]
    for instance in INSTANCES:
        if instance["challenge_id"] == challenge_id:
            break
    else:
        instance = None

    if instance is not None:
        uri = f"{challenge['proto']}://{instance['host']}:{instance['port']}"
        return jsonify(
            success=False,
            msg=f"You already have an instance running for this challenge at {uri}",
        )

    return jsonify(
        success=True, msg="Your request has been sent, please refresh the page."
    )

if __name__ == "__main__":
    app.run()