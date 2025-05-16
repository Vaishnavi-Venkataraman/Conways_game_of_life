# Conway’s Game of Life

> **Conway’s Game of Life** is a mesmerizing zero-player game — a **cellular automaton** where cells evolve based on simple rules of life and death and initial state of the grid.  

## Game Rules

The simulation follows four simple rules that determine how cells live or die in each generation:

-  **Underpopulation:** Any live cell with fewer than two live neighbors dies.
-  **Survival:** Any live cell with two or three live neighbors survives.
-  **Overpopulation:** Any live cell with more than three live neighbors dies.
-  **Birth:** Any dead cell with exactly three live neighbors becomes a live cell.

## Features

- Infinite grid using a `set` for live cells  
- 500 random initial cells in an 800x700 Pygame window  
- 15x15 pixel cells, updating every second  
- Displays current generation count on screen

## Requirements

- Python 3  
- Pygame (install using `pip`)
