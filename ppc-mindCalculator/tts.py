#%%
from websocket import create_connection
import subprocess
# from deepspeech import Model
import numpy as np
import wave
import re
from word2number import w2n

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import json

# %%
# ds = Model(r"deepspeech-0.9.3-models.pbmm")
# ds.enableExternalScorer(r"deepspeech-0.9.3-models.scorer")
keywords = (
    "what is negative plus minus and "
    "twenty thirty forty fifty sixty seventy eighty ninety hundred thousand "
    "eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen "
    "one two three four five six seven eight nine ten "
).split()
# for k in keywords:
#     ds.addHotWord(k, 2.5)

SetLogLevel(0)
# if not os.path.exists("model"):
#     print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
#     exit (1)
model = Model("model")

def recog(path):
    wf = wave.open(path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate(), f'["{" ".join(keywords)}", "[unk]"]')
    rec.SetWords(True)
    # rec.SetPartialWords(True)
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    res = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            resjson = rec.Result()
            print("RESU", resjson)
            res += " " + json.loads(resjson)["text"]
        # else:
            # print("PART", rec.PartialResult())

    # print("FINAL")
    resjson = rec.Result()
    print(resjson)
    res += " " + json.loads(resjson)["text"]
    res = res.replace("[unk] ", "")
    res = re.sub(r"(\w+) \1 ", r"\1 ", res)
    # print(repr(res))
    return res

# %%
def calculate():
    # fin = wave.open(r"a.wav", 'rb')
    # fs_orig = fin.getframerate()
    # audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
    # fin.close()
    # result = ds.stt(audio).strip()
    result = recog(r"a.wav").strip()

    print("heard =", repr(result))
    print("non-keywords =", *(i for i in result.split() if i not in keywords))

    ws = re.findall(r"(what is|plus|minus) (negative )?((?:(?:" + "|".join(i+' ' for i in keywords[5:]) + r"))+)", result + " ")

    try:
        calculated = 0
        for op, sym, num in ws:
            print(num)
            num = w2n.word_to_num(num)
            print(op, sym, num, end=" = ")
            if op == "minus":
                num *= -1
            if sym == "negative ":
                num *= -1
            print(num)
            calculated += num
        print("=", calculated)
    except Exception as e:
        print("error", e)
        return 0
    return calculated

#%%
# c = calculate()
# exit(0)


ws = create_connection("wss://mindcalculator.projectsekaictfdemo.1a23.studio/echo")
# ws = create_connection("ws://127.0.0.1:8080/echo")
ws.send("start")
while True:
    data = b""
    prompt = "0"
    while True:
        d = ws.recv()
        if type(d) == str:
            print("PROMPT:", d)
            prompt = d
            # if d:
            #     print("HALT")
            #     exit(0)
            continue
        if not d:
            break
        data += d

    # %%
    with open(r"a.mp3", "wb") as f:
        f.write(data)
    #%%
    subprocess.run(["ffmpeg", "-i", r"a.mp3", "-acodec", "pcm_s16le", "-ac", "1", "-ar", "16000", "-y", r"a.wav"])
    c = calculate()
    ws.send(str(c))
