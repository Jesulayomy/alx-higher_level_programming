from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

s1 = Square(2)
s2 = Square(3)

r1 = Rectangle(4, 2)
r2 = Rectangle(3, 1)

Base.draw([r1, r2], [s1, s2])
