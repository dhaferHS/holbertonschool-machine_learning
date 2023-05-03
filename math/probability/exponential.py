#!/usr/bin/env python3
"""Exponential that represents an exponential distribution"""


class Exponential:
    """Exponential distribution class"""
    def __init__(self, data=None, lambtha=1.):
        self.lambtha = float(lambtha)
        if data is None:
            if lambtha <= 0.0:
                raise ValueError("lamdtha must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain at least two values")
            self.lambtha = 1.0 / (sum(data) / float(len(data)))
