import matplotlib.pyplot as plt
import numpy as np

def create_subplot(data, ax=None):
    if ax is None:
        ax = plt.gca()
    bp = ax.imshow(data)
    return bp

# make figure with subplotsnp.array([[1,2,3],[4,5,6],[7,8,9]])
data=
#f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(10,5))
fig,ax=plt.subplots()
bp=create_subplot(data, ax)
