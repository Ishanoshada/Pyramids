# Pyramids: Unveiling Ancient Marvels

![Pyramids](https://img.shields.io/badge/Pyramids-Exploration-brightgreen)

## Table of Contents

- [About](#about)
- [History of Pyramids](#history-of-pyramids)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Data Analytics](#data-analytics)
- [Contributing](#contributing)

## About

Welcome to the Pyramids project, where we embark on a journey to explore the mysteries and grandeur of pyramids from across the world. This repository isn't just about scripts and data; it's a portal to unlock the enigma of these ancient structures.

## History of Pyramids


Pyramids, synonymous with Egypt, are architectural wonders that have captivated humanity for millennia. These colossal structures were built as tombs for pharaohs and monarchs, housing their mortal remains while serving as gateways to the afterlife. The history of pyramids is a testament to human ingenuity and engineering prowess.

- **The Great Pyramid of Giza**: Standing on the Giza Plateau, the Great Pyramid is one of the Seven Wonders of the Ancient World. It was constructed over 4,500 years ago, and its precise alignment with the cardinal points and mathematical precision continue to baffle researchers.

- **Pyramid of Khafre**: Adjacent to the Great Pyramid, the Pyramid of Khafre is slightly smaller but equally awe-inspiring. Its striking facade retains some of the original casing stones, offering a glimpse into the past.

- **Pyramid of Menkaure**: This pyramid, the smallest of the Giza trio, is a testament to the evolution of pyramid design over time.

But Egypt isn't the sole keeper of pyramid secrets. Across the Atlantic, in Mexico, stands Teotihuacan, a city of pyramids that bewilder archaeologists.

- **Pyramid of the Sun**: The Pyramid of the Sun in Teotihuacan is one of the largest pyramids in the world. Its construction required immense labor and serves as a testament to the spiritual and architectural prowess of its builders.

- **Pyramid of Kukulcán**: In Chichen Itza, Mexico, the Pyramid of Kukulcán showcases the Mayan civilization's understanding of celestial events. It's designed with precision to align with the equinoxes, casting shadows that resemble a descending serpent.

The world is dotted with pyramids, each telling a unique story of its civilization. The Pyramids project aims to delve into these stories and analyze their geometric and historical significance.

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

## Examples

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

## Data Analytics

The `Pyramids.json` file is a treasure trove of information. With the power of Python and data analysis libraries, you can uncover insights about these ancient structures.

You can explore aspects such as:

- **Historical Trends**: Analyze the heights and base lengths of pyramids over time to identify trends in architectural evolution.

- **Geographical Distribution**: Visualize the distribution of pyramids on a world map to see where these structures are concentrated.

- **Statistical Analysis**: Conduct statistical analyses to discover correlations between pyramid attributes like height, base length, and location.

- **Slope Angle Insights**: Examine slope angles to understand the design principles employed by ancient builders.

By applying data analytics techniques, you can shed light on the historical and architectural significance of pyramids worldwide.

## Contributing

Contributions are welcome! If you'd like to improve or expand this project, please feel free to submit pull requests.

