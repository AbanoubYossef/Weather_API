
# Django Weather App


## Overview

The Django Weather App is a simple web application that allows users to check the weather forecast for cities around the world. It provides real-time weather data and displays it in an easy-to-read format.

## Features

- **Weather Forecast**: Users can enter the name of a city to get the current weather forecast.
- **Detailed Information**: The app provides information such as temperature, humidity, pressure, visibility, and more.
- **OpenWeatherMap API**: Weather data is retrieved from the OpenWeatherMap API.
- **Database Storage**: Data for each city is stored in a PostgreSQL database.
- **City Watchlist**: Users can add multiple cities to their watchlist for quick access to weather updates.

## Prerequisites

Before you begin, make sure you have the following:

- **Python 3.x**: You should have Python 3.x installed on your machine.
- **PostgreSQL**: The app uses a PostgreSQL database to store city data.
- **OpenWeatherMap API Key**: You need an API key from OpenWeatherMap to fetch weather data. You can [sign up here](https://openweathermap.org/api) to obtain an API key.

## Installation

Follow these steps to set up and run the Django Weather App:

1. Clone the Repository:

   ```bash
   git clone https://github.com/yourusername/django-weather-app.git
   ```

2. Navigate to the Project Directory:

   ```bash
   cd django-weather-app
   ```

3. Create a Virtual Environment and Activate It:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a PostgreSQL Database:

   - Create a PostgreSQL database and update the database settings in `settings.py`.

6. Apply Database Migrations:

   ```bash
   python manage.py migrate
   ```

7. Configure OpenWeatherMap API Key:

   - Obtain an API key from OpenWeatherMap and add it to the `settings.py` file.

8. Start the Development Server:

   ```bash
   python manage.py runserver
   ```

9. Access the Application:

   Open your web browser and go to `http://localhost:8000` to access the application.

## Usage

1. Open the application in your web browser.
2. Enter the name of the city for which you want to check the weather.
3. Click the "Get Weather" button.
4. The weather forecast for the entered city will be displayed on the page.


---

This README provides comprehensive information about the Django Weather App, its installation, usage, and contribution guidelines. Feel free to modify it as needed for your project.
