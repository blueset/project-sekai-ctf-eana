import matplotlib
import matplotlib.pyplot as plt
from itertools import groupby
import numpy as np

# tshark -r osu.pcap -Y 'usbhid.data' -T fields -e usb.src -e usbhid.data

path = "osu1.txt"
ds = [i.split("\t") for i in open(path).read().splitlines()]
data = [(i, bytes.fromhex(j)) for i, j in ds]

mode = 0
modes = sorted(set(i[1] for i in data if i[0] == "1.30.1"))
colors0 = {
    0: "#B71C1C",
    129: "#E0E0E0",
    128: "#33691E",
}
colors1d = {
    0: "#B71C1C",
    129: "#B71C1C",
    128: "#00838F",
}
colors1b = {
    0: "#B71C1C",
    129: "#D84315",
    128: "#37474F",
}
colors = colors0

x = y = 0
letters = []

minx = float("inf")
maxx = float("-inf")
miny = float("inf")
maxy = float("-inf")
# mina = float("inf")
# maxa = float("-inf")

X = []
Y = []
C = []
for dev, payload in data:
    if dev == "1.30.1":
        x = payload[2] + payload[3] * 256
        y = payload[4] + payload[5] * 256
        a = payload[6] + payload[7] * 256
        # mina = min(mina, a)
        # maxa = max(maxa, a)
        a = int(a / 5292 * 255)
        ahex = hex(a)[2:].zfill(2)
        if a == 0: ahex = "06"
        c = colors[payload[1]] + ahex
        X.append(x)
        Y.append(-y)
        C.append(c)
        minx = min(minx, x)
        maxx = max(maxx, x)
        miny = min(miny, -y)
        maxy = max(maxy, -y)
    elif dev == "1.22.1":
        if payload[2] == 0x1b:
            colors = colors1b
        elif payload[2] == 0x1d:
            colors = colors1d
        else:
            colors = colors0
# print(mina, maxa)


# letters.append((X,Y,C))
# print(len(letters))
fig = plt.figure() 
ax = plt.axes(xlim=(minx, maxx), ylim=(miny, maxy)) 
sct = ax.scatter([], [], c=[], marker=".") 


# initialization function 
def init(): 
    # creating an empty plot/frame 
    sct.set_offsets(np.c_[[], []])
    return sct, 

# animation function 
def animate(i): 
    start = max(0, i-1000)
    sct.set_offsets(np.c_[X[start:i], Y[start:i]])
    sct.set_color(C[start:i])
    return sct, 

ani = matplotlib.animation.FuncAnimation(fig, animate, 
                init_func=init,
                frames=range(0, len(X), 20), interval=1, repeat=False) 
# plt.show()
ani.save('anim.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
