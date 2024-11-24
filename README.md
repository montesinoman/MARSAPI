# MARSAPI

A Python library for collecting information from the MethaneData API on methane emissions that it is published by [IMEO/MARS](https://methanedata.unep.org/map?sector=&company=&country=&cc=&sat=&limit=1000&pub=#mcoord=1.43/0/0)

![Build Status](https://img.shields.io/badge/under%20development-8A2BE2)

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)
5. [License](#license)

## Installation

Clone the repo:
```
git clone https://github.com/montesinoman/MARSAPI.git
```

Install the dependencies:
```
pip install -r requirements.txt
```

Run the setup script:
```
python setup.py install
```

## Usage

Display the plume shapefiles:
```
from marsapi import plumes
import folium

# Import the plumes
plumes = plumes.list_plumes()

# Show on a map
m = folium.Map()
folium.GeoJson(img_coords).add_to(m)
m
```

## Feature

- Import ready-to-use information by MARS about methane emissions
- Easy to work with commonly used data types as `DataFrames` or `GeoJSON`

## Contributing

We welcome contributions! Here is how you can help:
1. Fork the repository.
2. Create a branch for your feature:
```bash
git checkout -b feature-name
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
