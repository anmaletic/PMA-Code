import matplotlib.pyplot as plt
fig, a = plt.subplots(2,2)
import numpy as np
x = np.arange(0,1000)
a[0][0].plot(x,x+2)
a[0][0].set_title('linearna funkcija y=x+2')
a[0][1].plot(x,x**2)
a[0][1].set_title('kvadratna funkcija y=x**2')
plt.show() #u Jupyter notebook ne treba ova linija kôda
