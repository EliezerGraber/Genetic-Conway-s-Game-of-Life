import copy

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
    old_cells = copy.deepcopy(self.cells)
    for x, colls in enumerate(old_cells):
      for y, cell in enumerate(colls):
        count = self.neighbor_count(x, y, old_cells)
        #print(count, end = "")
        if (count == 3 and old_cells[x][y] == 0) or ((count > 3 or count < 2) and old_cells[x][y] == 1):
          self.toggle_cell(x, y)
      #print()

  def neighbor_count(self, x, y, c):
    count = 0
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or (i == x and j == y):
          continue
        #print(x,y,i,j,c[i][j])
        if c[i][j] == 1:
          #print(x,y,i,j)
          count +=1
    return count

  def toggle_cell(self, x, y):
     self.cells[x][y] = 1 - self.cells[x][y]




world = World(10, 10)
world.toggle_cell(4,4)
world.toggle_cell(4,5)
world.toggle_cell(4,6)
world.toggle_cell(5,5)
for x in range(15):
  world.print_world()
  world.evolve()
  print()
print(world.neighbor_count(2,3,world.cells))

