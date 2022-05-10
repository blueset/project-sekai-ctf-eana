from scipy.io import wavfile
import numpy as np
import random

min16 = np.iinfo(np.int16).min
max16 = np.iinfo(np.int16).max

voice_sr, voice_s = wavfile.read("test.wav")

samp = []
for i in voice_s:
    while True:
        base = random.randint(min16 + 1, max16 - 1)
        rev_base = -base
        if random.randint(0, 1):
            if not (min16 < base + i < max16):
                continue
            base += i
        else:
            if not (min16 < rev_base + i < max16):
                continue
            rev_base += i
        if random.randint(0, 1):
            base, rev_base = rev_base, base
        samp.append((base, rev_base))
        break

npsamp = np.array(samp, dtype=np.int16)
wavfile.write("test_noisy.wav", voice_sr, npsamp)
