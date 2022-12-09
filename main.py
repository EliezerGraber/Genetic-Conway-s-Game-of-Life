import copy

class World:
  def __init__(self, x = None, y = None, *, cells = None):
    self.rows = x if x else len(cells[0])
    self.cols = y if y else  len(cells)
    self.cells = cells if cells else [[0]*x for i in range(y)]

  def print_world(self):
    for rows in self.cells:
       for cell in rows:
          print("." if cell == 0 else "0", end = "")
       print()

  def evolve(self):
    old_cells = self.copy()
    for x, column in enumerate(old_cells.cells):
      for y, cell in enumerate(column):
        count = len(old_cells.neighbor_count(x, y))
        #print(count, end = "")
        if (count == 3 and old_cells.cells[x][y] == 0) or ((count > 3 or count < 2) and old_cells.cells[x][y] == 1):
          self.toggle_cell(x, y)

  def neighbor_count(self, x, y):
    neighbors = []
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or (i == x and j == y):
          continue
        #print(x,y,i,j,c[i][j])
        if self.cells[i][j] == 1:
          #print(x,y,i,j)
          neighbors.append([i,j])
    return neighbors

  def toggle_cell(self, x, y):
     self.cells[x][y] = 1 - self.cells[x][y]

  def copy(self):
     return World(cells = copy.deepcopy(self.cells))


class Lifebook:
  def __init__(self, world):
    self.world = world
    self.lifeforms = {}
  
  def life_check(self, time):
    buf = self.world.copy()
    lifeforms = []
    for x, col in enumerate(buf.cells):
      for y, cell in enumerate(col):
        if cell:
          form = [[x,y]]
          buf.toggle_cell(x,y)
          form = self.neighbor_check(x, y, buf, form)
          lifeforms.append(form)
    self.lifeforms[time] = lifeforms
            
  def neighbor_check(self, x, y, buf, form):
    neighbors = buf.neighbor_count(x, y)
    for neighbor in neighbors:
      form.append(neighbor)
      buf.toggle_cell(neighbor[0], neighbor[1])
      self.neighbor_check(neighbor[0], neighbor[1], buf, form)
    else:
      return form

  def delocalize(self, lifeforms):
    buf = copy.deepcopy(lifeforms)
    for form in buf:
      xmin = self.world.cols
      ymin = self.world.rows
      for coord in form:
        xmin = coord[0] if coord[0] < xmin else xmin
        ymin = coord[1] if coord[1] < ymin else ymin
      for coord in form:
        coord[0] -= xmin
        coord[1] -= ymin
    return [i for n, i in enumerate(buf) if i not in buf[:n]]
        
  def time_track_forms(self, lifeforms_ta, lifeforms_tb):
    for form_tb in lifeforms_tb:
      for form_ta in lifeforms_ta:
        for cell in form_tb:
          if cell in form_ta:
            pass
            #add to form of ta
          else:
            pass
            #create new form







world = World(10, 10)
lifebook = Lifebook(world)
world.toggle_cell(4,4)
world.toggle_cell(4,5)
world.toggle_cell(4,6)
world.toggle_cell(5,5)
for x in range(15):
  lifebook.world.print_world()
  lifebook.world.evolve()
  print()
#print(world.neighbor_count(2,3,world.cells))
lifebook.life_check(0)
print(lifebook.lifeforms[0])
print(lifebook.delocalize(lifebook.lifeforms[0]))