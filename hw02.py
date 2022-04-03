import enum
import numpy as np


class Direction(enum.Enum):
    Up = (0, -1)
    Right = (1, 0)
    Down = (0, 1)
    Left = (-1, 0)
    Still = (0, 0)


class Solution:
    def __init__(self, maze, width, height):
        self.maze = maze
        self.width = width
        self.height = height
        self.indexed_maze = dict()

        for x in range(width):
            for y in range(height):
                point = self.maze[x][y]
                if point in self.indexed_maze:
                    self.indexed_maze[point].append((x, y))
                else:
                    self.indexed_maze[point] = [(x, y)]
        print

    def print_maze(self, maze):

        for y in range(self.height):
            for x in range(self.width):
                print(maze[x][y], end=' ')
            print("")
        print("")

    def depth_first_limited_search(self, depth: int, action_block: int, action_direction: Direction):

        self.action_move(action_block, action_direction)
        if depth == 0:
            self.print_maze(self.maze)
            return
        possible_set = self.get_possible_move()
        tmp_maze = np.array(self.maze)
        for possible in possible_set:
            self.print_maze(self.maze)
            self.maze = tmp_maze
            self.print_maze(self.maze)
            self.depth_first_limited_search(
                depth-1, possible[0], possible[1])

    def action_move(self, action_block: int, action_direction: Direction):

        for point in self.indexed_maze[action_block]:
            x, y = tuple(map(sum, zip(action_direction.value, point)))
            self.maze[x][y] = 0
            self.maze[point[0]][point[1]] = 0

        # clear action_block's indexed_maze
        points = self.indexed_maze[action_block]
        self.indexed_maze[action_block] = []

        for point in points:
            x, y = tuple(map(sum, zip(action_direction.value, point)))
            self.maze[x][y] = action_block
            self.indexed_maze[action_block].append((x, y))

        print(action_block)
        print(action_direction)

    def get_possible_move(self):
        check_set = set()
        possible_set = set()
        for location in self.indexed_maze[0]:
            x = location[0]
            y = location[1]
            neighbors = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
            neighbors = filter(
                lambda item:
                    0 < item[0] < self.width and
                    0 < item[1] < self.height and
                    not (item[0] == 0 and item[1] == 0),
                neighbors,
            )
            for neighbor in neighbors:
                if neighbor[0] > x:
                    dir = Direction.Left
                elif neighbor[0] < x:
                    dir = Direction.Right
                elif neighbor[1] > y:
                    dir = Direction.Up
                else:
                    dir = Direction.Down

                check_set.add((self.maze[neighbor], dir))

        # traverse all neighbor
        for check in check_set:
            isPossible = True
            for point in self.indexed_maze[check[0]]:
                x, y = tuple(map(sum, zip(point, check[1].value)))
                target_point = self.maze[x][y]
                if target_point != check[0] and target_point != 0:
                    isPossible = False
                    break
            if isPossible:
                possible_set.add(check)

        return possible_set


if __name__ == "__main__":

    maze = np.array([[1, 2, 2, 3],
                     [1, 2, 2, 3],
                     [5, 5, 0, 6],
                     [4, 8, 0, 6],
                     [4, 7, 9, 10],
                     ])
    maze = np.swapaxes(maze, 0, 1)

    s = Solution(maze, 4, 5)
    action = (0, Direction.Still)
    s.depth_first_limited_search(1, 0, Direction.Still)
