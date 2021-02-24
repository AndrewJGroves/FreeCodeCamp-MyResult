class Rectangle:
  width=None
  height=None

  def __init__(self,wid,hi):
    self.width=wid
    self.height=hi

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self,value):
    self.width=value
  def set_height(self,value):
    self.height=value

  def get_amount_inside(self,shape):
    test=shape.get_area()
    test1=self.get_area()
    return int(test1/test)

  def get_picture(self):
    if(self.width > 50 or self.height > 50):
      return "Too big for picture."
    else:
      pic=""
      for i in range(self.height):
        pic+="*"*self.width
        pic+="\n"
      return pic

  def get_area(self):
    return self.width*self.height
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

class Square(Rectangle):
  def __init__(self, side):
    Rectangle.width = side
    Rectangle.height = side
  def __str__(self):
    return f"Square(side={self.width})"
  def set_side(self, value):
    Rectangle.set_width(self,value)
    Rectangle.set_height(self,value)
