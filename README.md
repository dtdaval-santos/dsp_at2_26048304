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
The Streamlit Web App has the following elements:

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

### Environment Setup

This project was built with **Python 3.9.6**. Using a different major version may cause package installs to fail or behave differently, so matching this version is recommended.

1. Create a virtual environment

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

If successful, your terminal prompt shows `(venv)` at the start of the line.

2. Install dependencies

With the venv active:

```bash
pip install -r requirements.txt
```

3. NOTE: what has been summarised in requirements.txt

`requirements.txt` states every package this app needs with the exact version it was built on and tested with (`package==version`). \
Installing with `-r requirements.txt` reproduces that in the virtual environment from Step 1, rather than pulling whatever the latest release of each package happens to be — which matters for reproducibility, since a newer major version of a library can change or remove behaviour this app depends on.

Only two packages were installed directly; everything else in the file (e.g., numpy, pandas, pyarrow) is a sub-dependency that `pip` pulled in automatically to support those two:

| Package | Version | Purpose |
|---|---|---|
| `streamlit` | 1.50.0 | Web app framework — builds the UI |
| `requests` | 2.32.5 | Makes HTTP calls to the Frankfurter API |

4. Run the app

```bash
streamlit run app.py
```

## How to Run the Program
<Provide instructions and examples>

## Project Structure
<List all folders and files of this project and provide quick description for each of them>

The project has the following files:

--> app.py: main Streamlit python script used for managing users’ inputs and displaying results \
--> api.py: python script that will contain the code for making API calls \
--> frankfurter.py: python script that will contain the functions used for calling relevant Frankfurter endpoints and extracting information. \
--> currency.py: python script that will contain the function used for formatting the results to be displayed in the Streamlit app. \
--> README.md: a markdown file containing your details (full name, student id), a description of this project, listing of all Python functions and instructions for running your web app 

## Citations
<Mention authors and provide links code you source externally>

This program calls 3 different API endpoints from the Frankfurter app:

--> Extracting the list of available currency codes (documentation: https://www.frankfurter.app/docs/#currenciesLinks to an external site.) \
--> Extracting the latest conversion rate for the specified currency codes (documentation: https://www.frankfurter.app/docs/#latestLinks to an external site.) \
--> Extracting the historical conversion rate for the specified currency codes and a given date (documentation: https://www.frankfurter.app/docs/#historicalLinks to an external site.)