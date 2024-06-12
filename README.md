# Hue Color Sorting using Python with A* Algorithm

## Introduction
This project is a simple implementation of the A* algorithm to sort colors by hue. The project is written in Python and uses the Image library to read and write images. The A* algorithm is used to sort the colors by hue, and will create a 
matrix of color sorted by its gradient.

## Requirements
- Python 3.6 or higher

## Installation
1. Clone the repository
2. Install the required libraries using the following command:
```bash
pip install -r requirements.txt
```

## Usage
1. Go to src folder using `cd src`
2. If you want to generate a starting image with given matrix, use Generator.py. You can modify the matrix anything you want. Run the following command:
```bash
python Generator.py ColorImage.py
```
3. If you want to sort the colors in the image, use Solver.py. Run the following command:
```bash
python Solver.py Node.py ColorImage.py
```

NOTE: Make sure you save the size of a color box the same as generated
