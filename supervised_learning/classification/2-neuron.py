#!/usr/bin/env python3
"""supervised neuron file that recognise numbers using some trained data"""
import numpy as np


class Neuron:
    """class for supervised neuron"""

    def __init__(self, nx):
        """initialisation of the supervised neuron"""

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        elif nx < 1:
            raise ValueError("nx must be a positive integer")

        """declaring private instance attribute"""

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """getter for W"""
        return self.__W

    @property
    def A(self):
        """getter for A"""
        return self.__A

    @property
    def b(self):
        """getter for b"""
        return self.__b

    def forward_prop(self, X):
        """creating public method for forword propagation"""
        """calculating the forward propagation for the neuron"""
        Z = np.dot(
            self.__W,
            X) + self.__b  # perform matrix multiplication between __w ( the weight of the neuron ) and  X THE INPUT data
        """creating and calcualtig the activation function for the neuron system"""
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A
