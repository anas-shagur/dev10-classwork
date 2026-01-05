class Cyclist:
    MIN_POWER = 1.0
    MAX_POWER = 10.0

    def __init__(self, name, power):
        self._name = name
        # valid power range is 1-10
        self._power = min(max(power, Cyclist.MIN_POWER), Cyclist.MAX_POWER)

    @property
    def name(self):
        return self._name

    @property
    def power(self):
        return self._power


class Bicycle:
    # km/h
    MAX_VELOCITY = 40.0
    STANDARD_ACCELERATION = 5.0
    BONUS_ACCELERATION = 4.0

    def __init__(self, cyclist):
        if cyclist is None:
            cyclist = Cyclist("Anonymous", 1.0)
        self._cyclist = cyclist
        self._velocity = 0.0

    @property
    def cyclist(self):
        return self._cyclist

    @property
    def velocity(self):
        return self._velocity

    def accelerate(self):
        # between 0.0 and 0.9
        power_modifier = (self._cyclist.power - Cyclist.MIN_POWER) / Cyclist.MAX_POWER
        # between 0.0 and 3.6
        power_acceleration = Bicycle.BONUS_ACCELERATION * power_modifier
        # can't go faster than MAX_VELOCITY
        self._velocity = min(
            self._velocity + (Bicycle.STANDARD_ACCELERATION + power_acceleration),
            Bicycle.MAX_VELOCITY,
        )

    def brake(self):
        # can't go slower than 0 km/h
        self._velocity = max(0.0, self._velocity - 10.0)
