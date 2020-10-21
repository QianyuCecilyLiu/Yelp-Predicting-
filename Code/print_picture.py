# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

lena = mpimg.imread('./image/wordcloud.png') 
plt.figure(figsize=(15,15))
plt.imshow(lena) 
plt.axis('off') 
plt.show()
