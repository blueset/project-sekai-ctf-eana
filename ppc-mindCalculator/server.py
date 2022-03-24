import aiohttp
from aiohttp import web
import inflect
import random
import asyncio
import edge_tts

app = web.Application()
routes = web.RouteTableDef()

loop = asyncio.get_event_loop()
infl = inflect.engine()

voices = [
    "en-AU-NatashaNeural",
    "en-CA-ClaraNeural",
    "en-IN-NeerjaNeural",
    "en-IE-EmilyNeural",
    "en-NG-AbeoNeural",
    "en-PH-RosaNeural",
    "en-ZA-LeahNeural",
    "en-GB-SoniaNeural",
    "en-US-AriaNeural",
    "en-US-GuyNeural",
    "en-US-JennyNeural",
]

async def get_voice(words):
    communicate = edge_tts.Communicate()
    voice = random.choice(voices)
    try:
        async for i in communicate.run(words, voice=voice):
            if i[2] is not None:
                yield i[2]
    except Exception as e:
        raise

def generate_number(number):
    return infl.number_to_words(number).replace("minus", "negative").replace(",", "")

def generate_equation():
    count = 100
    numbers = [random.randint(-9999, 9999) for _ in range(count)]
    symbols = [1] + [random.choice([0, 1]) for _ in range(count - 1)]
    result = sum(i * j for i, j in zip(numbers, symbols))
    equation = [generate_number(numbers[0])]
    for i in range(1, count):
        if symbols[i] == 1:
            equation.append(', plus')
        else:
            equation.append(', minus')
        equation.append(generate_number(numbers[i]))
    return f"What is {' '.join(equation)}?", result

@routes.get("/")
async def hello_world(request):
    return web.FileResponse('./index.html')

@routes.get('/echo')
async def echo(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    try:
        counter = -1
        result = "start"
        async for msg in ws:
            if msg.type != aiohttp.WSMsgType.TEXT:
                await ws.send_str("ERR")
                break
            input_txt = msg.data
            if str(input_txt) != str(result):
                await ws.send_str("WRONG")
                return ws
            counter += 1
            if counter >= 100:
                break
            eqn, result = generate_equation()
            await ws.send_str(f"{counter}")
            async for data in get_voice(eqn):
                await ws.send_bytes(data)
        with open("flag.txt", "r") as f:
            flag = f.read()
        await ws.send_str(flag)
        return ws
    except Exception as e:
        return ws

app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app)