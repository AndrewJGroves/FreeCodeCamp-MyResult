import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
  """ Class that models balls in a hat probablistically """

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, number):
    balls_drawn = []

    if number >= len(self.contents):
      return self.contents
    # Pick a ball at random and remove from the bag
    for i in range(number):
      ball_picked = random.choice(self.contents)
      balls_drawn.append(ball_picked)
      self.contents.pop(self.contents.index(ball_picked))
  
    return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count=0

  expected_list = []

  for key, value in expected_balls.items():
    for x in range(value):
      expected_list += key.split()

  for n in range(num_experiments):
    trial = copy.deepcopy(hat)
    draw = trial.draw(num_balls_drawn)
    result = list((Counter(expected_list) - Counter(draw)).elements())
    if(len(result) == 0):
      count += 1
  return count / num_experiments