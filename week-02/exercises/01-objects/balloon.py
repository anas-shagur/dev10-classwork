import random

class Balloon:

    def __init__(self, color, psi=0.0):
        self._color = color
        self._psi = psi

    @property
    def color(self):
        return self._color

    @property
    def psi(self):
        if self.is_exploded():
            return float('inf')
        else:
            return self._psi
    
    def inflate(self):
        self._psi = self._psi + random.random() * 5.0

    def is_exploded(self):
        return self._psi > 16.0
