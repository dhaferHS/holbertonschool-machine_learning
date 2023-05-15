#!/usr/bin/env python3
""" file for binomial distribution tasks """


class Binomial:
    """class binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """initialize the binomial distribution"""
        self.n = n
        self.p = p
        if data is None:
            self.n = int(n)
            if self.n <= 0:
                raise ValueError("n must be a positive value")
            self.p = float(p)
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            successes = sum(data) / len(data)
            trials = (sum([(x - successes) ** 2 for x in data]) / len(data))
            self.p = 1 - (trials / successes)
            self.n = round(successes / self.p)
            self.p = successes / self.n
