import copy

class World:
  def __init__(self, x, y):
    self.rows = x
    self.cols = y
    self.cells = [[0]*x for i in range(y)]
    self.lifeforms = []

  def print_world(self):
    for rows in self.cells:
       for cell in rows:
          print("." if cell == 0 else "0", end = "")
       print()

  def evolve(self):
    old_cells = copy.deepcopy(self.cells)
    for x, column in enumerate(old_cells):
      for y, cell in enumerate(column):
        count = len(self.neighbor_count(x, y, old_cells))
        #print(count, end = "")
        if (count == 3 and old_cells[x][y] == 0) or ((count > 3 or count < 2) and old_cells[x][y] == 1):
          self.toggle_cell(x, y,self.cells)
      self.lifeforms = self.life_check()

  def neighbor_count(self, x, y, c):
    neighbors = []
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or (i == x and j == y):
          continue
        #print(x,y,i,j,c[i][j])
        if c[i][j] == 1:
          #print(x,y,i,j)
          neighbors.append([i,j])
    return neighbors

  def toggle_cell(self, x, y, cells):
     cells[x][y] = 1 - cells[x][y]

  def life_check(self):
    buf = copy.deepcopy(self.cells)
    lifeforms = []
    for x, col in enumerate(buf):
      for y, cell in enumerate(col):
        if cell:
          form = [[x,y]]
          self.toggle_cell(x,y,buf)
          form = self.neighbor_check(x, y, buf, form)
          lifeforms.append(form)
    return lifeforms
            
  def neighbor_check(self, x, y, buf, form):
    neighbors = self.neighbor_count(x, y, buf)
    for neighbor in neighbors:
      form.append(neighbor)
      self.toggle_cell(neighbor[0], neighbor[1], buf)
      self.neighbor_check(neighbor[0], neighbor[1], buf, form)
    else:
      return form

  def delocalize(self, lifeforms):
    buf = copy.deepcopy(lifeforms)
    for form in buf:
      xmin = self.cols
      ymin = self.rows
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
world.toggle_cell(4,4,world.cells)
world.toggle_cell(4,5,world.cells)
world.toggle_cell(4,6,world.cells)
world.toggle_cell(5,5,world.cells)
for x in range(15):
  world.print_world()
  world.evolve()
  print()
#print(world.neighbor_count(2,3,world.cells))
print(world.life_check())
print(world.delocalize(world.life_check()))
