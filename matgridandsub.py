# matplotlib grid

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20,40,60,80])
y=np.array([0,50,100,150,200])
plt.title('sports watch data')
plt.xlabel('average pulse')
plt.ylabel('calorie burnage')
plt.plot(x,y,'o--g',ms=20,mec='r',mfc='b')
plt.grid()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,20,40,60,30,10])
y=np.array([100,150,250,60,10,80])
plt.title('today share market')
plt.xlabel('average value')
plt.ylabel('todays rate')
plt.plot(x,y,'o--r',ms=20,mec='g',mfc='b')
plt.grid()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,30,40,80,20,10])
y=np.array([20,80,30,10,70,250])
plt.title('share market')
plt.xlabel('average value')
plt.ylabel('current value')
plt.plot(x,y,'o--g',ms=20,mec='r',mfc='g')
plt.grid(axis='x',color='r',linestyle='--')
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x=np.array([20,40,60,80,100])
y=np.array([100,150,200,250,20])
plt.title('market value')
plt.xlabel('today average')
plt.ylabel('today rate')
plt.plot(x,y,'o--r',ms=20,mec='g',mfc='b')
plt.grid(axis='x',color='y',linestyle='--')
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x=np.array([20,40,60,80,100])
y=np.array([100,150,200,250,20])
plt.title('market value')
plt.xlabel('today average')
plt.ylabel('today rate')
plt.plot(x,y,'o--r',ms=20,mec='g',mfc='b')
plt.grid(color='y',linestyle='--')
plt.show()


#subplot -> we can plot more graphs in single graph

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,10,20,30])
y=np.array([0,30,40,20])
plt.subplot(1,2,1)
plt.plot(x,y)
x=np.array([20,10,50,10])
y=np.array([10,30,40,10])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,30,40,80,10])
y=np.array([20,40,10,60,20])
plt.subplot(1,2,1)
plt.plot(x,y,'o--g',ms=20,mec='r',mfc='b')
plt.grid(color='b',linestyle='--')
x=np.array([10,50,40,10,30])
y=np.array([0,20,40,30,10])
plt.subplot(1,2,2)
plt.plot(x,y,'o--b',ms=20,mec='g',mfc='y')
plt.grid(color='y',linestyle='--')
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,40,50])
y=np.array([30,40,20,10])
plt.title('share market')
plt.xlabel('today range')
plt.ylabel('average rate')
plt.grid(color='g', linestyle='--')
plt.subplot(1,2,1)
plt.plot(x,y,'o--g',ms=20,mec='r',mfc='r')
x=np.array([20,40,10,0])
y=np.array([50,20,40,10])
plt.title('share market')
plt.xlabel('average rate')
plt.ylabel('today rate')
plt.grid(color='r',linestyle='--')
plt.subplot(1,2,2)
plt.plot(x,y,'o--b',ms=20,mec='y',mfc='g')
plt.show()



