class Submarine:
    """
    An underwater, submersible vehicle.
    Includes two behaviors:
    `dive`: go down a little deeper under water to a maximum depth
    `surface`: come up a little shallower to a minimum depth of sea level

    The submarine's current depth and pressure are available via properties.
    """

    def __init__(self, max_depth):
        self._max_depth = max_depth
        self._depth_in_meters = 0.0

    @property
    def depth_in_meters(self):
        return self._depth_in_meters

    def dive(self):
        # 1. Each dive should increase the depth by 3 meters.
        # Depth cannot exceed self._max_depth.
        pass

    def surface(self):
        # 2. Each surface should decrease the depth by 5 meters.
        # Minimum depth is 0.0 (sea level).
        pass

    @property
    def pressure_in_atmospheres(self):
        # 3. At sea level, pressure is 1 atmosphere.
        # Pressure increases by 1 atmosphere for every 10 meters.
        return 0.0
