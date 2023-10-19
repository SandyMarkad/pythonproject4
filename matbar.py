#matplotlib bars -> we can draw the graph with the help of bar function

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,2,4,6])
y=np.array([20,40,60,80])
plt.bar(x,y)
plt.show()

# for horizontal bar use barh function

import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
y=np.array([100,200,300,400,500])
plt.barh(x,y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
y=np.array([100,200,300,400,500])
plt.barh(x,y,color='red')
plt.show()


#for bars use heght

import matplotlib.pyplot as plt
import numpy as np
x=np.array([2,4,6,8,10])
y=np.array([10,20,30,40,50])
plt.bar(x,y,color='green')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([2,4,6,8,10])
y=np.array([10,20,30,40,50])
plt.title('growth rate')
plt.xlabel('year of growth')
plt.ylabel('year of growth')
plt.bar(x,y,color='pink')
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, width = 0.1)
plt.show()

