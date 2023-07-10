#!/usr/bin/env python3
import numpy as np

""" creating a class for the neural network from scratch """


class NeuralNetwork:
    """ initializing everything in the neural network """

    """ a public method iinitialization """

    def __init__(self, nx, nodes):
        """ nx is the number of inpute data """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        elif nx < 1:
            raise ValueError("nodes must be a positive integer")
            """ nodes is the number of nodes found in the hiden layer """

        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        elif nodes < 1:
            raise ValueError("nodes must be a positive integer")

        """ the weights vector for the hiden layer"""
        """ initialisied withe a random normal distribution value"""
        """ w1 is the connection between the inpute and the hiden layer """
        self.W1 = np.random.randn(nodes, nx)
        self.b1 = 0
        self.A1 = 0
        """ w2  is the connection between the hiden layer and the output"""
        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0
