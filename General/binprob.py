# -*- coding: utf-8 -*-
"""
Probability testing: Entropy and Gini Index

Created on Tue Jul 27 10:27:52 2021

@author: tahad
"""


# %% Creating functions
def GI(P_i, n_elements=2):
    """Calculates the Gini index based on the given probability P_i and
    the number of elements n_elements;
    n_elements to be used for non-binary systems"""
    import numpy as np
    Gini_index = 1 - P_i ** 2 - (1 - P_i) ** 2

    return Gini_index


def entropy(P_i, n_elements=2):
    """Calculates the Entropy based on the given probability P_i and
    the number of elements n_elements;
    n_elements to be used for non-binary systems"""
    import numpy as np
    S = -P_i * np.log2(P_i) - (1 - P_i) * np.log2(1 - P_i)

    try:
        S[np.isnan(S)] = 0
    except TypeError:
        print('Not an array')

    return S


# %% Using Numpy and functions
import numpy as np
x = np.linspace(0, 1, 201)          # Creating 201 datapoints between 1 and 0

y_GI = GI(x)         # Gini index calculation
y_S = entropy(x)     # Entropy calculation


# %% Plotting the data
import matplotlib.pyplot as plt

fig, plts = plt.subplots()
plts.plot(x, y_GI,
          label='Gini Index')
plts.plot(x, y_S,
          label='Entropy')
plts.plot(x, np.linspace(1, 1, 201))
plts.set_xlabel('Probability [P_A]')
plts.set_ylabel('Value')
plts.legend()

plt.show()

# These clear commends seem to not work
plt.cla()
plt.clf()
plt.close()