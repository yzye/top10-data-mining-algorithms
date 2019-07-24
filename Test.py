#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:43:01 2017

@author: yuzheye
"""

# Assignment 3, Part 1: Random Matrix Theory

import numpy as np
import scipy.linalg as LA
import matplotlib.pyplot as plt

n = 100  # size of matrices
t = 5000  # number of samples
v = np.empty((t, n))  # eigenvalue samples
v1 = np.empty(t)  # max eigenvalue samples
delta = 0.2  # histogram bin width

for i in range(t):

    # TASK 1.1.1
    # sample from GOE
    a = np.random.rand(n,n)
    s = (a+a.T)/2

    # TASK 1.1.2
    # compute eigenvalues
    evals = LA.eig(s)[0]

    # store eigenvalues
    v[i, :] = evals

    # TASK 1.2.1
    # sample from GUE
    a = np.random.rand(n,n)+np.random.rand(n,n)*1j
    s = (a+a.T)/2

    # TASK 1.2.2
    # compute eigenvalues
    evals = LA.eig(s)[0]

    # store maximum eigenvalue
    v1[i] = np.amax(evals)