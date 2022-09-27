import numpy as np
import matplotlib.pyplot as plt


def plotear_temperaturas(file): 
    temperaturas = np.load(file) 
    plt.hist(temperaturas,bins=50)
    plt.show()


plotear_temperaturas('../Data/temperaturas.npy')