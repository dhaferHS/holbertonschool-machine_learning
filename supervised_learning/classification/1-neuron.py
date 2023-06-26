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
        """public instance"""
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
        """private instance"""

        self.__w = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

        def get_w(self):
            return self.__w

        def get_A(self):
            return self.__A

        def get_b(self):
            return self.__b
