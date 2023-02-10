#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(20, 7, 4, 2)
    r1.display()

    print("---")

    r1 = Rectangle(1, 1)
    r1.display()
