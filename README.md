# FX Currency Converter for 94692 Data Science Practice

## Author
Name: Dominique Daval Santos \
Student ID: 26048304

## Description
<What your application does>

This is a Web App using Streamlit where users can select 2 currencies and an amount to be converted. The goal of this program is to display the current conversion rate between 2 currency codes at a specific date or for the latest date. It will also calculate the inverse conversion rate between these 2 currencies. After selection the app will display the latest conversion rate, the converted amount and the inverse conversion rate. Additionally users can select a date in the past in order to get the conversion for this day. \

This application was created in fulfilment of 94692 Data Science Practice 2026 Spring Semester Assignment 2. As such, some docstrings and comments reflect the fact that the functions and logic were created in a way that meets project requirements.

The Streamlit Web App has the following elements:

- A number input where user can enter the amount to be converted \
- A select box listing all the currencies available on Frankfurter \
- A second select box listing all the currencies available on Frankfurter \
- A button that will fetch the latest conversion rate for the selected currencies \
- A text box that will display the expected text described previously \
- A date input where user can select a date in the past \
- A text box that will display the expected text described previously

Known limitations

- Loading time: the chart for historical rate trends may take a while to load depending on internet connection and calling 3 years of conversion rates on the API. when tested by the developer, it took around 5-20 seconds for different combinations of currencies.
- Same currency pair: Selecting the same currency for both "From" and "To" (e.g. AUD → AUD) will return an error. Frankfurter's API rejects this combination (HTTP 422) rather than returning a trivial 1:1 rate, so the app surfaces this as a normal error message rather than a crash.
- Weekends or holidays: will return the rates for the effective rates on that day from the latest trading day.
- Restricted inputs: no amount 0 or below and no future dates in the streamlit app, even though dates in the near future (a week or so) are accepted by the API.
- "Unable to fetch currency list" error: If this error appears, it usually means the initial call to Frankfurter's /currencies endpoint failed on load (often a transient network hiccup). Rather than refreshing the browser tab, use Streamlit's built-in Rerun — either the ⋮ menu in the top-right corner, or the R keyboard shortcut. This re-executes the script over the app's existing session rather than tearing down and reconnecting the whole browser tab from scratch, so it's the faster and more reliable way to retry. If it persists after a couple of Reruns, don't keep pressing R — quit and relaunch the app in the terminal instead (see the next point below).
- API intermittency: Frankfurter itself can be slow or time out on occasion, independent of this app's code or the user's own internet connection. This was confirmed during development — the exact same request sometimes succeeded and sometimes timed out within seconds of each other, tested from separate networks. A single failed request is not necessarily a sign of a bug.
- Repeated errors: if 3 or more consecutive requests return an error (whether from "Get Latest Rate" or "Conversion Rate"), this points to a longer-lasting issue (e.g. the Frankfurter API itself being down, or a local network/firewall problem) rather than a one-off transient failure. In this case, quit the app in the terminal (Control+C on Mac, Ctrl+C on Windows) and relaunch it with `streamlit run app.py` instead of continuing to retry within the same session.

<Some of the challenges you faced>
I placed this project on Github so I can practice using the technology, so it took more time to learn it and create branches than to just build the app and submit the zip folder.
It was also my first time to make a streamlit app outside of the few lines in the class labs and U:PASS sessions, so there was some trial and error.
Honestly, writing the README file and the elaborate docstrings and comments was more tedious than the code.
But debugging was a close second to the documentation in level of challenge.
Frankfurter's API itself also timed out a few times while testing historical rates, which initially looked like a bug in my own code before I confirmed (by re-testing the identical request) that the API was just being slow or unresponsive at that moment.

<Some of the features you hope to implement in the future>
Future versions of this app will have st.session_state implemented to persist the outputs of clicking both Latest and Historical Rates. \
Install the watchdog module in the virtual environment so the warning does not show up at "streamlit run app.py"

## How to Run the Program
<Provide instructions and examples>

### How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
<Which Python version you used>
<Which packages and version you used>

#### Environment Setup

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

### Using the App
<text here>

Note: Expected Streamlit quirk, not a bug: clicking "Conversion Rate" after already clicking "Get Latest Rate" will make the latest-rate section's output disappear from the page. \
The whole script reruns on every interaction, and st.button(...) only evaluates True on the exact run right after its own click.

streamlit run app.py

control + C for Mac
Ctrl + C for Windows

## Project Structure
<List all folders and files of this project and provide quick description for each of them>

The project has 4 modules. Note that more details like parameters and elaborate docstrings are inside the files, not in this README. The module files are as follows:

### app.py: 
main Streamlit python script used for managing users’ inputs and displaying results \

### api.py: python script that will contain the code for making API calls
explain the function inside it, when does it get called (i.e., what action on the app uses it)
get_url: call the API (www.frankfurter.app) and handle errors. \
only passes values from the functions in other files, which partially comes from the streamlit app's user input.

### frankfurter.py: python script that will contain the functions used for calling relevant Frankfurter endpoints and extracting information.
explain the functions inside it, when does it get called (i.e., what action on the app uses it) \
get_currencies_list \
get_latest_rates \
get_historical_rate \
get_rate_trend (with inherited logic from get_historical_rates)

### currency.py: python script that will contain the function used for formatting the results to be displayed in the Streamlit app.
round_rate \
reverse_rate \
format_output

### README.md: 
The markdown file you are reading (this line is so meta)

## Citations
<Mention authors and provide links code you source externally>

This program calls 3 different API endpoints from the Frankfurter app:

- Extracting the list of available currency codes (documentation: https://www.frankfurter.app/docs/#currenciesLinks to an external site.) \
- Extracting the latest conversion rate for the specified currency codes (documentation: https://www.frankfurter.app/docs/#latestLinks to an external site.) \
- Extracting the historical conversion rate for the specified currency codes and a given date (documentation: https://www.frankfurter.app/docs/#historicalLinks to an external site.)

Status codes can be looked up in the IETF's official HTTP Semantics standard documentation

- Go to https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes
-- Proceed to Section 15. Status Codes

AI Declaration: Claude (Anthropic) was used to help generate efficient code. README inclusions, docstring edits and edge-case handling were the ideas of the student.