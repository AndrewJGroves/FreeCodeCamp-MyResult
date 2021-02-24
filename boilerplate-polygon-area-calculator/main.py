# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(3, 6)
sq = shape_calculator.Square(5)

rect.set_width(7)
rect.set_height(8)
sq.set_side(2)
print(str(rect))
#expected = "Rectangle(width=7, height=8)"
print(str(sq))
#expected = "Square(side=2)"

sq.set_width(4)
print(str(sq))
#expected = "Square(side=4)"


# Run unit tests automatically
main(module='test_module', exit=False)