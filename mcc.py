import numpy as np
import math
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
import matplotlib.animation as animation
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker

insidecount = 0
totalcount = 0

fig, ax = plt.subplots(1,2,figsize=(10, 4))
ax[0].set_xlim(0,1)
ax[0].set_ylim(0,1)
#add some space between plots
fig.subplots_adjust(wspace=0.35)
#remove numbers and ticks from left graph
ax[0].xaxis.set_major_locator(plt.NullLocator())
ax[0].yaxis.set_major_locator(plt.NullLocator())
ax[1].set_xlabel('Number of Points')
ax[1].set_ylabel('Calculated Pi')
patches = []

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
    ax[0].set_title('Number of Points = {}'.format(t+1))
    pi = 4*insidecount/totalcount
    ax[1].plot(t,pi,'k.')
    ax[1].set_title('Approimate Pi = {:.3f}'.format(pi))

#draw the circle
circle = Circle((.5,.5), .5, facecolor='none', edgecolor='k')
ax[0].add_patch(circle)

#there are issues if the number of frames got to 1000
ani = animation.FuncAnimation(fig, update, interval = 1,  frames=300, save_count=300)
ani.save('MonteCarloCircle.mp4',fps=30)
#plt.show()