# matplotlib scatter

import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40])
y=np.array([0,30,40,20])
plt.scatter(x,y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,50,10])
y=np.array([20,10,50,10])
plt.scatter(x,y)
plt.show()




import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,2,4,6,8])  # years
y=np.array([60,70,80,90,100])  # speed
colors=np.array([10,20,30,40,50])
plt.scatter(x,y,c=colors,cmap='Blues')
x=np.array([0,2,4,6,8])
y=np.array([60,70,80,90,100])
colors=np.array([10,20,30,40,50])
plt.scatter(x,y,c=colors,cmap='viridis')
plt.show()




import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,2,3,4,5,6])
y=np.array([60,70,80,90,100,12])
plt.title('car time value')
plt.xlabel('car years')
plt.ylabel('cars spedd')
colors=np.array([10,20,30,40,50,60])
plt.scatter(x,y,c=colors,cmap='Blues')
plt.show()



