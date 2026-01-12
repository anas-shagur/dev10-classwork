class Power:

    def __init__(self, name):
        self._name = name
        pass

    @property
    def name(self):
        return self._name
    
class Hero:

    def __init__(self, name, powers = []):
        self._name = name
        self._powers = powers
        pass

    @property
    def name(self):
        return self._name
    
    @property
    def powers(self):
        return self._powers
    
    # 1. Create a new method in the Hero class.
# Name: to_line
# Inputs: none (self)
# Output: String
# Description: returns the Hero's name and powers as a single line of text.

    def to_line(self):
        power_names = ", ".join(power.name for power in self._powers)
        return f"{self._name}, Powers: {power_names}"