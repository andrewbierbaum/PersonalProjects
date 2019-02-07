import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import math

insidecount = 0
outsidecount = 0

fig, ax = plt.subplots(1,2,figsize=(10, 4))
ax[0].set_xlim(0,1)
ax[0].set_ylim(0,1)


def f(t):
    x=np.random.rand(1)
    y=np.random.rand(1)
    return x,y

def update(t):
    x,y = f(t)
    global insidecount
    global outsidecount
    # optionally clear axes and reset limits
    #plt.gca().cla() 
    #ax.set_xlim(0,1)
    #ax.set_ylim(0,1)
    distance = math.sqrt((x-0.5)*(x-0.5)+(y-0.5)*(y-0.5))
    if distance < 0.5:
        ax[0].plot(x,y, 'r.')
        insidecount += 1
    else:
        ax[0].plot(x,y,'b.')
        outsidecount += 1
    ax[0].set_title(str(t))
    if outsidecount>0:
       pi = insidecount/outsidecount
    else:
       pi = 0
    ax[1].plot(t,pi,'k.')
    ax[1].set_title('approimate Pi = {:.4f}'.format(pi))



ani = matplotlib.animation.FuncAnimation(fig, update, interval = 1,  frames=1000)
plt.show()