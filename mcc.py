#todo: speed improvement using ffmpeg writter
#lines between points
#multiple passes
#faster with blitting https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/speeding-up-the-plot-animation


import numpy as np
import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt

insidecount = 0
totalcount = 0

fig, ax = plt.subplots(1,2,figsize=(10, 4))
ax[0].set_xlim(0,1)
ax[0].set_ylim(0,1)


def rando(t):
    x=np.random.rand(1)
    y=np.random.rand(1)
    return x,y

def update(t):
    x,y = rando(t)
    global insidecount
    global totalcount
    distance = math.sqrt((x-0.5)*(x-0.5)+(y-0.5)*(y-0.5))
    if distance < 0.5:
        ax[0].plot(x,y, 'r.')
        insidecount += 1
        totalcount += 1
    else:
        ax[0].plot(x,y,'b.')
        totalcount += 1
    ax[0].set_title(str(t))
    pi = 4*insidecount/totalcount
    ax[1].plot(t,pi,'k.')
    ax[1].set_title('approimate Pi = {:.4f}'.format(pi))


ani = animation.FuncAnimation(fig, update, interval = 1,  frames=1000)
plt.show()