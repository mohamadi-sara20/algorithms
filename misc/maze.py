class Cell:
    def __init__(self, val=1, seen=False):
        self.seen = seen
        self._val = val

    @property
    def val(self):
        return self._val
    
    @val.setter
    def val(self, val):
        self._val = val

    
class Maze:
    def __init__(self, n : tuple, blocked:list[tuple], start=(0,0), end=(0,0)):
        self.start = (0, 0)
        self.end = (5,5)
        self.x = n[0]
        self.y = n[1]
        self.maze_grid = self.create_maze(blocked_cells=blocked)


    def create_maze(self, blocked_cells: list[tuple]):
        print(self.x)
        print(self.y)
        self.maze_grid = [[Cell() for x in range(self.x)] for y in range(self.y)] 
        for b in blocked_cells:
            self.maze_grid[b[0]][b[1]].val = 0
        return self.maze_grid
    
    def win(self, position, end=(5,5)):
        return position[0] == end[0]-1 and position[1] == end[1]-1
    
    def move(self, origin, direction):
        x, y = origin
        if direction == 'u' and y+1 < self.y and self.maze_grid[x][y+1].val == 1 and not self.maze_grid[x][y+1].seen:
            # self.maze_grid[x][y+1].seen = True
            return (x, y+1)
        elif direction == 'r' and x+1 < self.x and self.maze_grid[x+1][y].val == 1 and not self.maze_grid[x+1][y].seen:
            # self.maze_grid[x+1][y].seen = True
            return (x+1, y)
        elif direction == 'd' and y-1 >= 0 and self.maze_grid[x][y-1].val == 1 and not self.maze_grid[x][y-1].seen:
            # self.maze_grid[x][y-1].seen = True
            return (x, y-1)
        elif direction == 'l' and x-1 >= 0 and self.maze_grid[x-1][y].val == 1 and not self.maze_grid[x-1][y].seen:
            # self.maze_grid[x-1][y].seen = True
            return (x-1, y)
        return
    
    def dfs_solve(self, origin, path):
        if self.win(origin):
            return True
        directions = ['u', 'r', 'd', 'l']
        self.maze_grid[origin[0]][origin[1]].seen = True
        for d in directions:
            position = self.move(origin, d)
            if not position:
                continue
            out = self.dfs_solve(position, path)
            if out:
                path.append(position)
                return True
            return False




if __name__ == "__main__":
    # maze = Maze(n=(5,5), blocked=[(0, 2), (1, 2), (1,0), (3,0), (2,1)], start=(0,0), end=(5,5))
    maze = Maze(n=(5,5), blocked=[(0, 2), (1, 2), (2,1)], start=(0,0), end=(5,5))
    print(maze)
    path = []
    x = maze.dfs_solve((0,0), path)
    path.append((0,0))
    print(path)