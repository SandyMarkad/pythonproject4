# matplotlib pie 

import matplotlib.pyplot as plt
import numpy as np
x=np.array([20,40,60,10])
plt.pie(x)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
mylabel=['apple','banana','cherry','kiwi','lemon']
plt.pie(x,labels=mylabel)
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
mylabel=['apple','banana','cherry','kiwi','lemon']
plt.pie(x,labels=mylabel)
plt.legend(title='five fruits')
plt.show()
