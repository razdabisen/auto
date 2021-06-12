# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:35:59 2020

@author: razdabisen
"""
import numpy as np
import matplotlib.pyplot as plt
#ex=np.arrange(2,10,2)
x=np.arrange(0,3*np.pi, 0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()