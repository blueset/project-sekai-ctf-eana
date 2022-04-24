# Mind Calculator Challenge

Can you keep all the numbers in your brain?

## Writeup
1. Run speech recognition against the audio received. Word-for-word recognition is preferred, this is to minimize misconversions of numbers by the speech recognition engine.
2. Revert words to numbers and calculate the result.
3. Send the calculation result back to the server.
4. Repeat 100 times with less than 20 errors to get the flag.

### Tested environments
* Vosk (model: `vosk-model-en-us-0.22-lgraph`). Speed: ~5s per question; Accuracy: ~85%.
* Azure Speech. Speed: ~20s per question; Accuracy: ~92%.
