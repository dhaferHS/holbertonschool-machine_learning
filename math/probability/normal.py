#!/usr/bin/env python3
"""class normal propability"""


class Normal:
    """class for normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """initialize the normal distribution"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            res = (sum([(x - self.mean) ** 2 for x in data]) / len(data)) ** 0.5
            self.stddev = res
