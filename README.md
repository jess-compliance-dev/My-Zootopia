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
🦁 Zootopia is a small web generator project that fetches animal data from an external API and builds a dynamic HTML website based on user input.

The program asks the user for an animal name, retrieves information from an API, and generates a styled website showing the results.
If the animal does not exist, a friendly error message is displayed in the generated page.

This project demonstrates working with APIs, environment variables, modular Python code, and dynamic HTML generation.

## Technologies
* Project is created with: Python version: 3.11+
* Libraries:
    * requests
    * python-dotenv
* HTML/CSS template for displaying animal cards
* External animal API
* .env file for storing API key securely
  
## Features
* Ask the user for an animal name
* Fetch animal data from an external API
* Modular structure:
  * animals_web_generator.py → website generator
  * data_fetcher.py → API communication
* Generate HTML cards dynamically for all returned animals
* Display:
  * Name
  * Scientific name
  * Type
  * Location
  * Lifespan
  * Temperament
  * Weight
  * Diet
* Error handling:
 * If no animal is found → show styled message in website
* Use environment variables for API key security
* Requirements file for easy setup

## Setup
1. To install this project, simply clone the repository and install the dependencies in requirements.txt using pip:
````
  git clone https://github.com/yourusername/zootopia.git
  cd zootopia
  pip install -r requirements.txt
````
3. Make sure Python 3.11+ is installed:
````
$ python --version
````
5. Create .env file in the root folder:
````
   API_KEY=insert_your_API_key
````
## Usage
1. Run the script:
````
  $ python animals_web_generator.py
````
2. You will be asked which animal you would like to have info for. Type any animal.
````
3. You will see: Website was successfully generated to the file animals.html.
````
4. Open animals.html in your browser to see the result.
5. If the animal doesn't exist, you will see an error message in the website.

## Project Purpose
This project is designed for learning:
* Working with APIs in Python
* Using environment variables (.env)
* Structuring code into modules
* Generating HTML dynamically
* Handling user input
* Error handling and fallback messages
* Using Git & GitHub
* Managing dependencies with requirements.txt

## Requirement file
requirements.txt contains:
````
requests
python-dotenv
````
To be installed with:
```
pip install -r requirements.txt
```
