"""
Troy Brunette
BFS / DFS

This is a Maze Solving Program that uses a Breadth First Search algorithm to solve the maze. 
The bfs algorithm uses a Queue data structure to keep track of the nodes that need to be explored.


Algorithm:
    * Start at an initial node
    * Visit node
    * Explore neighbors
    * check for unvisited neighbors
    * visit neighbor node/s
    * if no more unvisited neighbors, go back to previous node
    * Repeat until all nodes are visited

Pseudocode:
def depth_first_search(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    order = []

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            order.append(current)

            # Push neighbors onto the stack in the order they appear in the adjacency list
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return order

Time Complexity: O(V + E)

"""

import os
import time

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows, self.cols = len(maze), len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]

    def is_valid_move(self, row, col):
        return self.rows > row >= 0 == self.maze[row][col] and self.cols > col >= 0

    # kinda funky needs work
    def clear_terminal(self):
        os.system('' if os.name == 'nt' else 'clear')  # Clear terminal screen

    def solve(self, start, end):
        queue = Queue()
        queue.enqueue((start[0], start[1], 0, [start]))  # (row, col, steps, path)

        while not queue.is_empty():
            current_row, current_col, _, path = queue.dequeue()

            if (current_row, current_col) == end:
                print("Maze successfully completed!\n")
                print("Final Full Path:")
                self.display_maze_path(path)

                break

            if not self.visited[current_row][current_col]:
                self.visited[current_row][current_col] = True

                # Possible Direction Moves: UP, DOWN, LEFT, RIGHT
                moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for move in moves:
                    new_row, new_col = current_row + move[0], current_col + move[1]

                    if self.is_valid_move(new_row, new_col):
                        new_path = path + [(new_row, new_col)]
                        queue.enqueue((new_row, new_col, 0, new_path))
                        # time.sleep(0.2)  # Small pause for each step
                        # self.display_maze_path(new_path)
                        # self.clear_terminal()
                # print(path)
        else:
            print("No valid path exists to complete the maze.")

    def display_maze_path(self, path):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in path:
                    print("X", end=" ")  # X is the path taken
                elif self.maze[i][j] == 1:
                    print("#", end=" ")  # Barriers or Walls
                else:
                    print("0", end=" ")  # 0 for valid places to move
            print()
        print()


def read_maze_from_file(file_path):
    with open(file_path, 'r') as file:
        maze = [list(map(int, line.split())) for line in file.readlines()]
    return maze


def print_menu():
    print("1. Solve Maze")
    print("2. Import Maze from File")
    print("3. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            maze_file_path = 'mazes/examplemaze_2.txt'
            maze = read_maze_from_file(maze_file_path)

            start_position = (0, 0)
            end_position = (4, 4)  # Change the exit location

            maze_solver = MazeSolver(maze)
            maze_solver.solve(start_position, end_position)

        elif choice == "2":

            file_path = 'mazes'
            file = crawl_directory(file_path)
            # Read from the selected file
            with open(file, 'r') as f:
                content = f.read()
                print(f"Unsolved Maze:\n{content}")
            if os.path.exists(file):
                maze = read_maze_from_file(file)
                start_position = (0, 0)
                end_position = (len(maze)-1, len(maze[0])-1)  # Possibly Change the exit location

                maze_solver = MazeSolver(maze)
                maze_solver.solve(start_position, end_position)
            else:
                print("File not found. Please enter a valid file path.")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


def crawl_directory(path):
    # List all files in the directory
    files = os.listdir(path)
    return selection(path, files)


def selection(directory, files):
    # Print each file in directory
    print("Files:")
    for i, file in enumerate(files):
        print(f"- {i + 1}. {file}")

    # User Selects a file from the files listed
    # Ask the user to select a file
    while True:
        try:
            choice = int(input("Select a file by entering its number: ")) - 1

            if choice < 0 or choice >= len(files):
                print("!Please enter a valid number!")
            else:
                selected_file = os.path.join(directory, files[choice])

                # Read from the selected file
                return selected_file

        except ValueError:
            print("Try entering a number.")


if __name__ == "__main__":
    main()
