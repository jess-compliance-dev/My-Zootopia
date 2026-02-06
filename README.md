# 🦁 Zootopia

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Purpose](#project-purpose)

## General info
🦁 Zootopia is a small web project that showcases animal data in a clean, card-based layout generated from a JSON file.  
It demonstrates reading JSON, processing data, and dynamically generating HTML content.

## Technologies
Project is created with:
* Python version: 3.11+
* Standard Python library: `json`
* HTML/CSS for displaying the cards
* Local JSON file (`animals_data.json`) as data source

## Features
* Load and parse animal data from JSON
* Generate HTML cards for each animal including:
  * Name
  * Scientific name
  * Type
  * First location
  * Lifespan
  * Temperament
  * Weight
  * Diet
* Replace placeholders in HTML template (`animals_template.html`) automatically
* Handle special characters and formatting issues in the data

## Setup
1. Clone the repository and navigate into the folder:
  $ git clone https://github.com/yourusername/zootopia.git  
  $ cd zootopia

2. Make sure Python 3.11+ is installed:
  $ python --version

3. Ensure `animals_data.json` and `animals_template.html` are present in the project folder.

## Usage
1. Run the script:
  $ python main.py

2. After running, the script will generate an `animals.html` file with all animal cards populated.  
3. Open `animals.html` in your browser to view the card-based layout.

## Project Purpose
This project is designed as a **small web data visualization project** for learning:

* Reading and parsing JSON data in Python
* Generating dynamic HTML content from data
* Handling string formatting and special characters
* Displaying information in a clean, card-based layout
* Combining Python scripting with basic web technologies (HTML/CSS)

