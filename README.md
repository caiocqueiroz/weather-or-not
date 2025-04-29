# Weather Or Not

A simple command-line weather application that shows current weather conditions for your location or any US ZIP code.

## Features

- Get current weather conditions (temperature and sky conditions)
- Get wind conditions (Demo 1 only)
- Automatic location detection
- ZIP code lookup support
- No API keys required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/caiocqueiroz/weather-or-not.git
cd weather-or-not
```

2. Create a virtual environment and install dependencies:
```bash
# For Demo 1
cd "Demo 1/weather"
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

The application has two versions:
- Demo 1: Includes wind conditions
- Demo 2: Basic weather information

### Demo 1 Commands:
```bash
# Get weather for current location
python weather.py current

# Get weather for specific ZIP code
python weather.py current --zipcode 90210

# Get wind conditions
python weather.py wind

# Get location info
python weather.py where-is
```

### Demo 2 Commands:
Same as Demo 1 but without the wind command.

## APIs Used
- wttr.in for weather data
- zippopotam.us for ZIP code lookups
- ip-api.com for IP geolocation