#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 17:02:43 2018

@author: alexmartin
"""

import numpy as np
from scipy.linalg import toeplitz
from numpy.linalg import eigh
A = toeplitz([1, 2, 0, 2])
[Dint, Uint] = eigh(A)
# use eigh not eig for symmetric matrices
idx = Dint.argsort()[::-1]
D = Dint[idx]
U = Uint[:, idx]
print(np.allclose(U.dot(np.diag(D)).dot(U.T), A))