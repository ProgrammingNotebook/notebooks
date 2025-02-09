class _022_Class:
    """ This is a class that represents a rectangle. """

    def __init__(self, length = 0, breadth = 0):
        """ Creates a rectangle with no lenght and breadth. """
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return (self.length + self.breadth) * 2
