class World:
  def __init__(self, x, y):
    self.rows = x
    self.cols = y
    self.cells = [[0]*x for i in range(y)]

  def print_world(self):
    for rows in self.cells:
       for cell in rows:
          print("." if cell == 0 else "0", end = "")
       print()

  def evolve(self):
    pass

  def neighbor_count(self, x, y):
    count = 0
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        if i < 0 or i > self.rows or j < 0 or j > self.cols or (i == x and j == y):
          continue
        if self.cells[i][j] == 1:
          count +=1
    return count

  def toggle_cell(self, x, y):
     self.cells[x][y] = self.cells[x][y] - 1




world = World(10, 10)
world.toggle_cell(2,3)
world.print_world()
print(world.neighbor_count(2,2))

