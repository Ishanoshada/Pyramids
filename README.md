# Pyramids 

Explore the fascinating world of pyramids from different parts of the world, calculate their properties, and visualize their dimensions.

![Pyramids](https://img.shields.io/badge/Pyramids-Exploration-brightgreen)

## Table of Contents

- [About](#about)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)

## About

The Pyramids project allows you to work with pyramid data and perform various calculations related to their dimensions. It includes Python scripts to calculate volume, surface area, and other properties of pyramids, as well as a JSON file containing information about different pyramids from around the world.

## File Structure

```plaintext
Pyramids/
├── create_pyramidV1.py
├── create_pyramidV2.py
├── pyramids.py
├── Pyramids.json
└── README.md
```

- `create_pyramidV1.py`: Python script for calculating blocks needed for a specific pyramid.
- `create_pyramidV2.py`: Improved Python script for calculating pyramid properties with user input.
- `pyramids.py`: Python script for calculating pyramid properties with predefined dimensions.
- `Pyramids.json`: JSON file containing information about various pyramids.
- `README.md`: This README file.

## Installation

To use the provided Python scripts, make sure you have Python installed on your system.

## Usage

You can use the Python scripts to perform calculations on pyramids or explore the pyramid data in the JSON file. Refer to the specific script's usage instructions for details.


## Example Usage

### 1. Using pyramids.py

You can use the `pyramids.py` script to calculate the properties of a pyramid with custom dimensions. Here's an example:

```python
# Create an instance of a pyramid
my_pyramid = Pyramid(230.4, 146.6)

# Calculate and print its volume, surface area, and slope angle
print("Pyramid Base Length:", my_pyramid.base_length)
print("Pyramid Height:", my_pyramid.height)
print("Pyramid Volume:", my_pyramid.volume())
print("Pyramid Surface Area:", my_pyramid.surface_area())
print("Pyramid Slope Angle:", slope_angle(my_pyramid.height, my_pyramid.base_length))
```

### 2. Using create_pyramidV2.py

With `create_pyramidV2.py`, you can input your own pyramid dimensions and get calculations for a custom pyramid. Here's how:

```python
# Get user input for pyramid dimensions
base_length = float(input("Enter the base length of the pyramid (in meters): "))
height = float(input("Enter the height of the pyramid (in meters): "))
num_sides = int(input("Enter the number of sides of the pyramid: "))

# ... (follow the on-screen prompts)

# Display the results
print("Number of Blocks Needed:", every_decimal(blocks_needed))
print("Pyramid Volume:", every_decimal(user_pyramid.volume()))
print("Pyramid Slope Angle (degrees):", every_decimal(slope_angle_degrees))
```

### 3. JSON Data

You can access pyramid data in the `Pyramids.json` file. Here's an example of the data format:

```json
[
    {
        "name": "Great Pyramid of Giza",
        "height": 146.6,
        ...
    },
    {
        "name": "Pyramid of Khafre",
        "height": 136.4,
        ...
    },
    ...
]
```

### Calculations

#### Using `create_pyramidV1.py`

```bash
python create_pyramidV1.py
```

This script calculates the number of blocks needed to build a specific pyramid.

#### Using `create_pyramidV2.py`

```bash
python create_pyramidV2.py
```

This script allows you to input pyramid dimensions and calculates properties like volume and slope angle.

#### Using `pyramids.py`

```bash
python pyramids.py
```

This script calculates pyramid properties with predefined dimensions.

## Contributing

Contributions are welcome! If you'd like to improve or expand this project, please feel free to submit pull requests.

---

Feel free to customize this README according to your project's specific needs. Enjoy exploring the world of pyramids! 🏜️
