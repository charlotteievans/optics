import matplotlib.pyplot as plt
import numpy as np

def create_subplot(data, ax=None):
    if ax is None:
        ax = plt.gca()
    bp = ax.imshow(data)
    return bp



np.random.rand(100,100)

test=[1,2,3,4,5,6,7]
for i in test:
    fig = plt.figure()
    fig = plt.imshow(np.random.rand(100,100))
    cbar = plt.colorbar()
    cbar.set_label(r'Signal to Noise (significance $\sigma$)')
    plt.xlabel('X (arcmin)')
    plt.ylabel('Y (arcmin)')
    plt.title('Signal to Noise map')
    plt.savefig(str('%03d'%i)+'.png')
    plt.clf()