
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
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

#setup the writer
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib', comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)
fig = plt.figure()
l, = plt.plot([], [], 'k-o')
plt.xlim(0, 1)
plt.ylim(0, 1)

xpointsinside = []
ypointsinside = []
xpointsoutside = []
ypointsoutside = []

with writer.saving(fig, "MCC.mp4", 10):
    for i in range(10):
        x,y = random.random() 
        if math.sqrt((x-0.5)*(x-0.5)+(y-0.5)*(y-0.5)) < 0.5:
            xpointsinside.append(x)
            ypointsinside.append(y)
            plt.plot(xpointsinside,ypointsinside)
        else:
            xpointsoutside.append(x)
            ypointsoutside.append(y)
            plt.plot(xpointsoutside,ypointsoutside)

        writer.grab_frame()
        
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



