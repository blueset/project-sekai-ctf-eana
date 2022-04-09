from deepspeech import Model
import re
import numpy as np
import inflect
import wave
import edge_tts
import random
import subprocess
import asyncio
import json

infl = inflect.engine()

voices = [
    "en-AU-NatashaNeural", # 70
    "en-CA-ClaraNeural", # 70
    "en-IN-NeerjaNeural", # 70
    "en-IE-EmilyNeural", # 70
    "en-NG-AbeoNeural", # 20
    "en-PH-RosaNeural", # 100
    "en-ZA-LeahNeural", # 90
    "en-GB-SoniaNeural", # 100
    "en-US-AriaNeural", # 90
    "en-US-GuyNeural", # 70
    "en-US-JennyNeural", # 90
]

async def get_voice(words, voice):
    communicate = edge_tts.Communicate()
    try:
        async for i in communicate.run(words, voice=voice):
            if i[2] is not None:
                yield i[2]
    except Exception as e:
        raise

keywords = (
    "what is negative plus minus and "
    "twenty thirty forty fifty sixty seventy eighty ninety hundred thousand "
    "eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen "
    "one two three four five six seven eight nine ten "
).split()
# model = Model("/Users/blueset/Downloads/model")

ds = Model(r"/Users/blueset/Downloads/deepspeech-0.9.3-models.pbmm")
ds.enableExternalScorer(r"/Users/blueset/Downloads/deepspeech-0.9.3-models.scorer")

for k in keywords:
    ds.addHotWord(k, 2)

def recog(path):
    fin = wave.open(r"a.wav", 'rb')
    audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
    fin.close()
    res = ds.stt(audio).strip()
    
    return res.strip()

def generate_number(number):
    return infl.number_to_words(number).replace("minus", "negative").replace(",", "").replace("-", " ")

def generate_equation():
    count = 10
    numbers = [random.randint(-9999, 9999) for _ in range(count)]
    symbols = [1] + [random.choice([-1, 1]) for _ in range(count - 1)]
    result = sum(i * j for i, j in zip(numbers, symbols))
    print(*zip(numbers, symbols), sep="\n")
    equation = [generate_number(numbers[0])]
    for i in range(1, count):
        if symbols[i] == 1:
            equation.append(', plus')
        else:
            equation.append(', minus')
        equation.append(generate_number(numbers[i]))
    return f"what is {' '.join(equation)}", result

async def test(voice):
    eqn, result = generate_equation()
    with open("a.mp3", "wb") as f:
        async for data in get_voice(eqn, voice):
            f.write(data)
    eqn = eqn.replace(" , ", " ")
    subprocess.run(["ffmpeg", "-i", r"a.mp3", "-acodec", "pcm_s16le", "-ac", "1", "-ar", "16000", "-y", r"a.wav"])
    result = recog(r"a.wav")
    print("EQUATION")
    print(eqn)
    print("RESULT")
    print(result)
    print("MATCH", eqn == result)
    match_sans_and = eqn.replace(" and ", " ") == result.replace(" and ", " ")
    print("MATCH SANS AND", match_sans_and)
    return match_sans_and


async def main():
    values = []
    for _ in range(10):
        values.append(await test(voices[10]))
    print(values)


if __name__ == "__main__":
    asyncio.run(main())
