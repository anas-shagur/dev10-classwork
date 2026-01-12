class Musician:
    def __init__(self, name="", rating=5):
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
    
    @name.setter 
    def name(self, name):
        self._name = name

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        self._rating = rating
