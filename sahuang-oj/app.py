import requests
import json
import hashlib
from flask import Flask, request, render_template

from utils import *

app = Flask(__name__, template_folder="", static_folder='static',)

language_map = {
    "C": c_config['language_config'],
    "C++": cpp_config['language_config'],
    "Python3": py_config['language_config'],
    "Java": java_config['language_config'],
    "Go": go_config['language_config'],
    "JavaScript": js_config['language_config']
}

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/submit", methods=["POST"])
def submit():
    code = request.json["code"]
    language = request.json["language"]
    challenge_id = request.json["challengeId"]
    # time_limit = request.json["time_limit"]

    if not (0 <= challenge_id <= 2):
        return {"flag": None, "testCases": [{
            "status": "SYSTEM_ERROR",
            "output": "Invalid challenge ID",
        }]}

    time_limit = 1000
    problem_id = chals[challenge_id]

    # Send submission to Judge Server
    url = "http://20.124.204.46:2048/judge"
    headers = {
        "Content-Type": "application/json",
        "X-Judge-Server-Token": hashlib.sha256("SEKAI_OJ_PPC".encode('utf-8')).hexdigest()
    }
    body = {
        'src': code,
        'max_cpu_time': time_limit, 
        'max_memory': 268435456, 
        'test_case_id': problem_id, 
        'output': True, 
        'language_config': language_map[language],
        'io_mode': {'input': 'input.txt', 'output': 'output.txt', 'io_mode': 'Standard IO'}
    }
    r = requests.post(url, headers=headers, data=json.dumps(body))
    # pprint(r.json())
    if r.status_code != 200:
        return {"flag": None, "testCases": None, "message": "Server Error"}

    # Return result
    '''
    result field return value
    WRONG_ANSWER = -1 (this means the process exited normally, but the answer is wrong)
    SUCCESS = 0 (this means the answer is accepted)
    CPU_TIME_LIMIT_EXCEEDED = 1
    REAL_TIME_LIMIT_EXCEEDED = 2
    MEMORY_LIMIT_EXCEEDED = 3
    RUNTIME_ERROR = 4
    SYSTEM_ERROR = 5
    '''
    r = r.json()
    if r['err'] is not None:
        return {"flag": None, "testCases": [{
            "status": "COMPILE_ERROR",
            "output": r['err'] + "\n" + r['data'],
        }]}

    ac = True
    status_map = {
        -1: "WRONG_ANSWER",
        0: "SUCCESS",
        1: "CPU_TIME_LIMIT_EXCEEDED",
        2: "REAL_TIME_LIMIT_EXCEEDED",
        3: "MEMORY_LIMIT_EXCEEDED",
        4: "RUNTIME_ERROR",
        5: "SYSTEM_ERROR"
    }
    test_cases = []
    for c in r['data']:
        if int(c["result"]) != 0:
            ac = False
            # RUNTIME_ERROR will print output such as "ReferenceError: rl is not defined"
            test_cases.append({
                "status": status_map[int(c["result"])],
                "output": c["output"] if c["result"] != -1 else "Wrong answer."
            })
        else:
            test_cases.append({
                "status": status_map[int(c["result"])],
                "timeMs": c["real_time"],
                "memoryKb": int(c["memory"]) // 1024,
            })
    flag = flag_map[problem_id] if ac else None

    return {"flag": flag, "testCases": test_cases}

if __name__ == "__main__":
    app.run(debug=False)
