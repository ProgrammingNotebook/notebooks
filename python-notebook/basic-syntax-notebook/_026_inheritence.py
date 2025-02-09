from _022_Class import _022_Class

class _026_Inheritence(_022_Class):
    """ This class represents the square """
    def __init__(self, side = 0):
        super().__init__(side, side)


square = _026_Inheritence(5)

print(square.area())
print(square.perimeter())
