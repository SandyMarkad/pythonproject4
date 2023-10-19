#plotting x and y points

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,10])
y=np.array([0,200])
plt.plot(x,y,)
plt.show()


# plotting without line

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20])
y=np.array([0,220])
plt.plot(x,y,'o')
plt.show()

# plotting multiple points

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20,50,30,10])
y=np.array([0,100,150,350,50])
plt.plot(x,y)
plt.show()

# default x points

import matplotlib.pyplot as plt
import numpy as np
y=np.array([0,100,150,350,50])
plt.plot(x,y)
plt.show()

# default x points

import matplotlib.pyplot as plt
import numpy as np
y=np.array([0,20,50,30,10,0])
plt.plot(y)
plt.show()

#  default y points

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20,50,30,10,0])
plt.plot(x)
plt.show()


