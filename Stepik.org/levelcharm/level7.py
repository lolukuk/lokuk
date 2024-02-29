class Integer:
    def __set_name__(self, owner, name):
        self.name = " " + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, ):

class Pains1:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть числом")


