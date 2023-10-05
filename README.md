# TWITTER-SENTIMENT-ANALYSIS-COVID-19
# Sentiment Analysis Project for Varcons Technologies

## Project Overview
This repository contains the code and resources for a sentiment analysis project developed during the internship at Varcons Technologies. The project aimed to predict sentiment based on keywords provided, utilizing machine learning techniques. It includes three models: Random Forest, Naive Bayes, and Logistic Regression. The sentiment analysis was performed on Twitter data using various Python libraries, including TextBlob for sentiment classification, NLTK for text processing, and Flask for creating a user-friendly web interface to display the results.

## Project Highlights

- *Sentiment Prediction Models:* Implemented machine learning models - Random Forest, Naive Bayes, and Logistic Regression to predict sentiment based on provided keywords.
  
- *Data Collection:* Scraped Twitter data to create a diverse dataset for training and testing the models.
  
- *Data Preprocessing:* Utilized TextBlob for sentiment classification, performed label encoding for sentiment extraction, and applied NLTK tools like lemmatization and stemming for text processing.
  
- *User-Friendly Web Interface:* Developed a user-friendly web interface using Flask to interact with the models. Users can input keywords and choose from the three available models, and the web app displays the predicted sentiment and accuracy.
  
- *Model Deployment:* Loaded trained models using pickle files and deployed them on the local host using Flask at the backend.

The web interface will be accessible at `http://localhost:5000`.

## Project Structure

- *`app.py`*: Contains the Flask application code for handling user requests and displaying results.

- *` models/`*: Directory containing the trained machine learning models saved as pickle files.

- *` data/`*: Directory to store the scraped Twitter data and other relevant datasets.

- *`utils/`*: Utility functions for data preprocessing, model training, and evaluation.

- *`templates/`*: HTML templates for rendering the web interface.

- *`static/`*: Static files  for enhancing the user interface.

## Technologies Used
- *Python(3.9.10)*: Core programming language for data analysis, machine learning, and web development.

- *Flask*: Web framework used for creating the user interface and handling backend operations.

- *TextBlob*: Python library for processing textual data, including sentiment analysis.

- *NLTK*: Natural Language Toolkit used for text processing tasks like lemmatization and stemming.

- *Pickle*: Python library for serializing and deserializing Python objects, used to save and load machine learning models.

## Acknowledgements
Special thanks to Varcons Technologies for providing the opportunity to work on this project during the internship. The project benefited from the open-source community and various Python libraries and tools used for development.

Feel free to explore the code, provide feedback, and contribute to further improvements!

