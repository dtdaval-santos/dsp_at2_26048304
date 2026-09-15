# FX Currency Converter for 94692 Data Science Practice

## Author
Name: Dominique Daval Santos \
Student ID: 26048304

## Description
<What your application does>
<Some of the challenges you faced>
<Some of the features you hope to implement in the future>

This is a Web App using Streamlit where users can select 2 currencies and an amount to be converted. The goal of this program is to display the current conversion rate between 2 currency codes at a specific date or for the latest date. It will also calculate the inverse conversion rate between these 2 currencies. \
After selection the app will display the latest conversion rate, the converted amount and the inverse conversion rate. \
Additionally users can select a date in the past in order to get the conversion for this day. \
The Streamlit Web App has the following elements: \\
--> A number input where user can enter the amount to be converted \
--> A select box listing all the currencies available on Frankfurter \
--> A second select box listing all the currencies available on Frankfurter \
--> A button that will fetch the latest conversion rate for the selected currencies \
--> A text box that will display the expected text described previously \
--> A date input where user can select a date in the past \
--> A text box that will display the expected text described previously \\
Future versions of this app will have __

## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
<Which Python version you used>
<Which packages and version you used>

## How to Run the Program
<Provide instructions and examples>

## Project Structure
<List all folders and files of this project and provide quick description for each of them>

The project has the following files: \\
--> app.py: main Streamlit python script used for managing users’ inputs and displaying results \
--> api.py: python script that will contain the code for making API calls \
--> frankfurter.py: python script that will contain the functions used for calling relevant Frankfurter endpoints and extracting information. \
--> currency.py: python script that will contain the function used for formatting the results to be displayed in the Streamlit app. \
--> README.md: a markdown file containing your details (full name, student id), a description of this project, listing of all Python functions and instructions for running your web app 

## Citations
<Mention authors and provide links code you source externally>

This program calls 3 different API endpoints from the Frankfurter app: \\
--> Extracting the list of available currency codes (documentation: https://www.frankfurter.app/docs/#currenciesLinks to an external site.) \
--> Extracting the latest conversion rate for the specified currency codes (documentation: https://www.frankfurter.app/docs/#latestLinks to an external site.) \
--> Extracting the historical conversion rate for the specified currency codes and a given date (documentation: https://www.frankfurter.app/docs/#historicalLinks to an external site.)