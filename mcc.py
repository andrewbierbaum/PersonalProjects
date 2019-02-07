import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import math

def f(t):
    x=np.random.rand(1)
    y=np.random.rand(1)
    return x,y

fig, ax = plt.subplots()
ax.set_xlim(0,1)
ax.set_ylim(0,1)

def update(t):
    x,y = f(t)
    # optionally clear axes and reset limits
    #plt.gca().cla() 
    #ax.set_xlim(0,1)
    #ax.set_ylim(0,1)
    if math.sqrt((x-0.5)*(x-0.5)+(y-0.5)*(y-0.5)) < 0.5:
        ax.plot(x,y, 'r.')
    else:
        ax.plot(x,y,'b.')
    ax.set_title(str(t))

ani = matplotlib.animation.FuncAnimation(fig, update, interval = 1,  frames=1000)
plt.show()