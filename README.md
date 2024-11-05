# Personal Water Tracker Project
A fully interactive dashboard created with Python and HTML and styled with CSS. Courtesy of Pyscript.

# Personal Water Tracker Project

## Overview
This project is a personal water intake tracker that monitors daily water consumption. I tracked my water intake over three months, stored it in an Excel file, and analyzed the data using Python. A real-time dashboard was created using Python, HTML, and Bootstrap CSS, facilitated by the Pyscript framework. A detailed guide on how to recreate this project can be found on my [website](https://diseph.medium.com/python-dashboard-web-app-with-pyscript-2024-9fb7d65c9f25).

## Table of Contents
1. [Why I Built It](#why-i-built-it)
2. [Why Pyscript?](#why-pyscript?)
3. [What I Learned](#what-i-learned)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Data Source](#data-source)
7. [Structure of the Repo](#structure-of-the-repo)
8. [Insights](#insights)
9. [Images](#images)
10. [Contact](#contact)

## Why I Built It
I created this water intake tracker to monitor and improve my daily water consumption. After my doctor advised that my water intake was low, I decided to build a dashboard that would allow me to monitor intake patterns and update my progress in real-time, helping me stay accountable. 

## Why Pyscript?
I chose Pyscript for this project because I wanted to experiment with a new Python web framework, since I had prior experience with Django and Flask. I aimed to build a lightweight application that could run seamlessly in a browser and could be easily shared with others who might benefit from similar tracking.

## What I Learned
Working on this project taught me:
- How to use Pyscript for building web-based applications with Python.
- The integration of Plotly data visualization in third-party web frameworks.
- Transporting variables from Python to HTML, by manipulating the Document Object Model (DOM).

## Features
- **Real-Time Dashboard**: The app updates in real-time with new water intake data, allowing for continuous monitoring.
- **Interactive Charts**: Data visualization with Plotly provides interactive and customizable charts that make it easy to spot trends and patterns.
- **Responsive Design**: Built with Bootstrap CSS, the dashboard is fully responsive, adapting to various screen sizes for accessibility on mobile devices.
- **Personal Insights**: By displaying key metrics like monthly intake and daily averages, the app provides a clear summary of progress over time.

## Technologies Used
- **Backend**: Python (Pyscript), Pandas, Numpy
- **Frontend**: HTML, Bootstrap CSS
- **Visualization**: Plotly for creating interactive charts
- **DOM Manipulation**: Pyodide (JavaScript module)
- **Hosting**: GitHub Pages

## Data Source
The primary data source was a three-month log of daily water intake that I manually entered into an Excel file. This data includes timestamps, volume intake, and other relevant details. I used Pandas to clean and organize the raw data, and stored it in a structured CSV format to allow for real-time updates on the dashboard.

## Structure of the Repo
- **[Assets](/assets)**: Contains images and CSS styling for background and other UI elements.
- **[Data](/data)**: Includes raw and cleaned data files.
- **[Scripts](/scripts)**: Contains the Python script used to clean and preprocess the data.
- **[App](/app.py)**: The main Python script powering the dashboard.
- **[Index](/Index.html)**: The HTML file for the app interface.

## Insights
The data analysis provided some key insights into my water intake habits:
1. **High Intake in January**: My water intake was at its highest in January, likely due to New Year’s motivation and conscious effort toward improving my health.
2. **Morning Intake Patterns**: I tend to drink more water in the mornings, which correlates with my daily exercise routine. This habit indicates that physical activity significantly impacts my hydration levels.
3. **Drop in March**: My intake was at its lowest in March, largely due to a busy schedule that often led to missed or delayed tracking. This period taught me the importance of consistent tracking.
4. **Data Accuracy Challenges**: Since the data was manually entered, some errors are inevitable. Delayed entries often relied on my memory, which sometimes led to inaccuracies, such as double-counting intake. This limitation highlights the potential value of automatic tracking systems for more accurate data.

These insights help reinforce the need for consistent hydration, especially after physical activity, and underscore the importance of reliable tracking methods to reduce human error.

## Images


## Contact
Feel free to reach out with questions or feedback. If via email, use the repository title as the subject.
