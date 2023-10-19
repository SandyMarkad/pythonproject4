# matplotlib markers -> you can draw line with various symbol of markers
# there are variou types of symbols which can we used to draw the plot.

import matplotlib.pyplot as plt
import numpy as np
y=np.array([0,20,40,60])
plt.plot(y,marker='o')     # marker stands for symbol of points
plt.show()


# There are various types of lines we can draw
#solid line '-'
# dotted line ':'
# dashed line '--'

import matplotlib.pyplot as plt
import numpy as np
y=np.array([0,40,20,50,30])
plt.plot(y,'o--')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
y=np.array([0,40,20,50,30])
plt.plot(y,'*--')
plt.show()


# There are various types of colours
# red blue green cyan magenta yellow black white
# we can use these colours for plotting the lines

import matplotlib.pyplot as plt
import numpy as np
y=np.array([0,40,20,50,30])
plt.plot(y,'o--r')  # points is o with dashed line and red colour
plt.show()


import matplotlib.pyplot as plt
import numpy as np
y=np.array([0,20,40,50,10])
plt.plot(y,'o--g')   # with green colour
plt.show()

#marker size -> we can give starting point or marker size as we want

import matplotlib.pyplot as plt
import numpy as np
y=np.array([0,10,50,30,40])
plt.plot(y,'o--b',ms=20)    #point is o with dashed line with blue colour and 20meter size
plt.show()


import matplotlib.pyplot as plt
import numpy as np
y=np.array([0,10,30,50,70,40,20,0])  # same as above
plt.plot(y,'o--b',ms=30)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,30,50,20])
y=np.array([0,30,60,40])
plt.plot(x,y,'o--g',ms=20)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20,50,30])
y=np.array([20,50,70,30])
plt.plot(x,y,'o--g', ms=20)
plt.show()



# marker edge colour

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20,40,60])
y=np.array([0,30,40,50])
plt.plot(x,y,'o--g',ms=20,mec='r')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,30,40,20,50])
y=np.array([0,20,40,60,80])
plt.plot(x,y,'o--g',ms=20,mec='r')
plt.show()


# marker face colour

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20,40,60])
y=np.array([0,30,40,50])
plt.plot(x,y,'o--b',ms=20,mec='r',mfc='g')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,30,40,20])
y= np.array([3, 8, 1, 10])
plt.plot(x,y,'o--b', ms = 20, mec = 'r', mfc = 'r')
plt.show()



import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '20.5')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20,10,30])
y=np.array([0,20,40,50])
z=np.array([0,30,40,10])
a=np.array([20,40,50,10])
plt.plot(x,y,z,a)
plt.show()





