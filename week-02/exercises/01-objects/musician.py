class Musician:
    def __init__(self, name, rating):
        """
        Args:
            name: The name of the musician.
            rating: A number representing how much a musician is loved relative to other musicians.
        """

        self._name = name
        self._rating = rating

    @property
    def name(self):
        return self._name
