import random
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="", static_folder='static',)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/submit", methods=["POST"])
def submit():
    code = request.json["code"]
    language = request.json["language"]
    print(code, language)
    correct = {
        "flag": "SEKAI{本気出すぞ_明日からにしよう_逃げた先は_ベッドの中_夢のつ•づ•き•を}",
        "testCases": [
            {"status": "correct", "timeMs": 427, "memoryKb": 39},
            {"status": "correct", "timeMs": 427, "memoryKb": 39},
            {"status": "correct", "timeMs": 427, "memoryKb": 39},
            {"status": "correct", "timeMs": 427, "memoryKb": 39},
            {"status": "correct", "timeMs": 427, "memoryKb": 39},
            {"status": "correct", "timeMs": 427, "memoryKb": 39},
            {"status": "correct", "timeMs": 427, "memoryKb": 39},
            {"status": "correct", "timeMs": 427, "memoryKb": 39},
        ]
    }
    wrong = {
        "flag": None,
        "testCases": [
            {"status": "correct", "timeMs": 427, "memoryKb": 39},
            {"status": "wrongAnswer", "timeMs": 427, "memoryKb": 39},
            {"status": "runTimeError", "timeMs": 427, "memoryKb": 39},
            {"status": "timeLimitExceeded", "timeMs": 999, "memoryKb": 39},
            {"status": "compilationError", "timeMs": 999, "memoryKb": 39},
        ]
    }
    return correct if random.randint(0, 1) else wrong

if __name__ == "__main__":
    app.run(debug=False)
