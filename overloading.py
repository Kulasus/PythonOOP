class Square:
    def __init__(self, side):
        self.side = side

    def __add__(squareOne, squareTwo):
        return ((squareOne.side * 4) + (squareTwo.side * 4))

squareOne = Square(5) # 5 * 4 = 20
squareTwo = Square(10) # 10 * 4 = 40
print("Sum of sides of both squares = ", squareOne + squareTwo)

