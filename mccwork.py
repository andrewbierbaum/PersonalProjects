
#%%
get_ipython().run_line_magic('matplotlib', 'inline')


#%%
#calculate and show the volume of a circle using montecarlo simulation
#place points withing a 1 by 1 square and test if they are withing a distance of 0.5 from the center 
#https://youtu.be/ThS4juptJjQ?t=1607 plot made
#https://youtu.be/ThS4juptJjQ?t=1561 animation

#directly from the srs https://github.com/matplotlib/matplotlib/tree/master/examples/animation
#2 clearly written examples http://www.labri.fr/perso/nrougier/teaching/matplotlib/#animation

import random
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#setup the writer
#FFMpegWriter = manimation.writers['ffmpeg']
#metadata = dict(title='Movie Test', artist='Matplotlib', comment='Movie support!')
#writer = FFMpegWriter(fps=15, metadata=metadata)
fig = plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)

#def animate(i):
for i in range(1000):
    x = random.random() 
    y = random.random()
    if math.sqrt((x-0.5)*(x-0.5)+(y-0.5)*(y-0.5)) < 0.5:
        plt.plot(x,y, 'r.',animated=True)
    else:
        plt.plot(x,y,'b.',animated=True)
       
#ani = animation.FuncAnimation(fig, animate, range(1, len(y)),interval=dt*1000, blit=True, init_func=init)

plt.show()

#anim = animation.FuncAnimation(fig,animation_frame,frames=100)

#anim.save('animation.gif', fps=4,extra_args=['-vcodec', 'libx264'])        
#print(insidepoints)
#print(outsidepoints)

#plt.Circle((.5,.5),radius = .5)


#%%



#%%



#%%



#%%



