# Sorting Algorithm Visualiser
This repository contains a Python script that visualises different sorting algorithms. The script uses the Pygame library to create a graphical representation of the sorting process.

## Features
Visualisation of different sorting algorithms
Ability to generate random lists for sorting
Customizable list size and value range
Adjustable sorting order (ascending or descending)

## Files
sortingAlgorithmVis.py: This is the main script that contains the implementation of the sorting algorithms and the visualisation logic.

## Classes
Drawinfo: This class is used to store information about the Pygame window and the list to be sorted. It also contains methods to set the list and calculate the dimensions of the bars representing the list elements.

## Functions
generate_random_list: This function generates a list of random integers within a specified range.
draw_list: This function draws the list on the Pygame window.
draw: This function draws the Pygame window and the controls for the visualiser.

## Usage
To run the visualiser, execute the sortingAlgorithmVis.py script. You can interact with the visualiser using the following controls:

R: Reset the list
Space: Start sorting
A: Sort in ascending order
D: Sort in descending order
1: Use Insertion Sort
2: Use Bubble Sort
3: Use Selection Sort

## Requirements
Python 3
Pygame

## Installation
- Clone the repository
- Install the requirements with pip install pygame
  ```pip3 install pygame``` or ```pip install pygame```
- Run the script with python sortingAlgorithmVis.py
  ```python sortingAlgorithmVis.py```

## License
This project is licensed under the MIT License.
