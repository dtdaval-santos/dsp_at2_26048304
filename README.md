# FX Currency Converter for 94692 Data Science Practice

## Author
Name: Dominique Daval Santos \
Student ID: 26048304

## Description

This is a Web App using Streamlit where users can select 2 currencies and an amount to be converted. The goal of this program is to display the current conversion rate between 2 currency codes at a specific date or for the latest date. It will also calculate the inverse conversion rate between these 2 currencies. After selection the app will display the latest conversion rate, the converted amount and the inverse conversion rate. Additionally users can select a date in the past in order to get the conversion for this day.

This application was created in fulfilment of 94692 Data Science Practice 2026 Spring Semester Assignment 2. As such, some docstrings and comments reflect the fact that the functions and logic were created in a way that meets project requirements.

#### The Streamlit Web App has the following elements:

- A number input where user can enter the amount to be converted
- A select box listing all the currencies available on Frankfurter
- A second select box listing all the currencies available on Frankfurter
- A button that will fetch the latest conversion rate for the selected currencies
- A text box that will display the expected text described previously
- A date input where user can select a date in the past
- A text box that will display the expected text described previously

#### Known limitations:

- **Loading time**: the chart for historical rate trends may take a while to load depending on internet connection and calling 3 years of conversion rates on the API. when tested by the developer, it took around 5-20 seconds for different combinations of currencies.
- **Same currency pair**: Selecting the same currency for both "From" and "To" (e.g. AUD → AUD) will return an error. Frankfurter's API rejects this combination (HTTP 422) rather than returning a trivial 1:1 rate, so the app surfaces this as a normal error message rather than a crash.
- **Weekends or holidays**: will return the rates for the effective rates on that day from the latest trading day.
- **Restricted inputs**: no amount 0 or below and no future dates in the streamlit app, even though dates in the near future (a week or so) are accepted by the API.
- **"Unable to fetch currency list" error**: If this error appears, it usually means the initial call to Frankfurter's /currencies endpoint failed on load (often a transient network hiccup). Rather than refreshing the browser tab, use Streamlit's built-in Rerun — either the ⋮ menu in the top-right corner, or the R keyboard shortcut. This re-executes the script over the app's existing session rather than tearing down and reconnecting the whole browser tab from scratch, so it's the faster and more reliable way to retry. If it persists after a couple of Reruns, don't keep pressing R — quit and relaunch the app in the terminal instead (see the next point below).
- **API intermittency**: Frankfurter itself can be slow or time out on occasion, independent of this app's code or the user's own internet connection. This was confirmed during development — the exact same request sometimes succeeded and sometimes timed out within seconds of each other, tested from separate networks. A single failed request is not necessarily a sign of a bug. This was also confirmed firsthand during testing: a request for AUD to USD on 2026-09-08 failed with an error, then succeeded cleanly about five minutes later with no code changes in between.
- **Repeated errors**: if 3 or more consecutive requests return an error (whether from "Get Latest Rate" or "Conversion Rate"), this points to a longer-lasting issue (e.g. the Frankfurter API itself being down, or a local network/firewall problem) rather than a one-off transient failure. In this case, quit the app in the terminal (Control+C on Mac, Ctrl+C on Windows) and relaunch it with `streamlit run app.py` instead of continuing to retry within the same session.

#### Challenges faced (personal student/developer notes):
- I placed this project on Github so I can practice using the technology, so it took more time to learn it and create branches than to just build the app and submit the zip folder.
- It was also my first time to make a streamlit app outside of the few lines in the class labs and U:PASS sessions, so there was some trial and error.
- Honestly, writing the README file and the elaborate docstrings and comments was more tedious than the code.
- But debugging was a close second to the documentation in level of challenge, especially when the error is from the code of a function called from a different module file. Errors ranged from typos, to missing arguments, to passing arguments in the proper order.
- Limitations were identified from software testing, not mere AI suggestions of what to write here.
- Frankfurter's API itself also timed out a few times while testing historical rates, which initially looked like a bug in my own code before I confirmed (by re-testing the identical request) that the API was just being slow or unresponsive at that moment.

#### Future Development:

- Future versions of this app will have st.session_state implemented to persist the outputs of clicking both Latest and Historical Rates.
- Install the watchdog module in the virtual environment so the warning does not show up at "streamlit run app.py"

This project is version-controlled and publicly hosted on GitHub at https://github.com/dtdaval-santos/dsp_at2_26048304. Future improvements to this app — including the `st.session_state` and `watchdog` items noted above — can be built by cloning the repository directly rather than working from the submitted zip file:

```bash
git clone https://github.com/dtdaval-santos/dsp_at2_26048304.git
cd dsp_at2_26048304
```

From there, follow the Environment Setup steps below to create the virtual environment and install dependencies before running the app.

## How to Run the Program

### How to Setup

#### Environment Setup

This project was built with **Python 3.9.6**. Using a different major version may cause package installs to fail or behave differently, so matching this version is recommended.

1. Create a virtual environment. If successful, your terminal prompt shows `(venv)` at the start of the line.

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
2. Install dependencies

   With the venv active:

   ```bash
   pip install -r requirements.txt
   ```
3. NOTE: what has been summarised in additional requirements.txt file that was not part of the project brief:

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

1. Launch the app from your terminal, with the virtual environment active:

   ```bash
   streamlit run app.py
   ```

   This opens the app automatically in your default browser (usually at `localhost:8501`).

2. Enter the amount to be converted. The input will not accept `0` or a blank/negative value — it's restricted to a minimum of `1`, so there's always a valid amount before clicking either rate button.

3. Make sure "From Currency" and "To Currency" are set to two different currencies. Selecting the same currency for both will return an error — Frankfurter's own API rejects that combination (see Known Limitations above).

4. Click "Get Latest Rate" for the current rate, or pick a date and click "Conversion Rate" for a historical rate. Each displays the formatted conversion sentence below its button.

    Note: Expected Streamlit quirk, not a bug: clicking "Conversion Rate" after already clicking "Get Latest Rate" will make the latest-rate section's output disappear from the page. \
The whole script reruns on every interaction, and st.button(...) only evaluates True on the exact run right after its own click.

5. To quit the app:

   In the terminal where it's running:

   ```bash
   Control + C   # Mac
   Ctrl + C      # Windows
   ```

## Project Structure

The project has 4 modules. Note that more details like parameters and elaborate docstrings are inside the files, not in this README. The module files are as follows:

### app.py
Main Streamlit script. Builds the UI — the amount input, the two currency select boxes, the date picker, and the two rate buttons — calls the relevant functions from `frankfurter.py` and `currency.py` in response to each button click, and displays either the formatted result or an error message.

### api.py
Contains `get_url`, the single function responsible for every HTTP request this app sends. It wraps `requests.get()` in a try/except block so network failures (no connection, DNS failure, timeout) are caught here once, rather than every function in `frankfurter.py` needing its own exception handling. Called indirectly by every function in `frankfurter.py` — never called directly from `app.py`.

### frankfurter.py
Contains the functions that call Frankfurter's three API endpoints and extract the data `app.py` needs from each response.

- `get_currencies_list`: fetches the full list of currency codes Frankfurter supports; used to populate both currency select boxes on app load.
- `get_latest_rates`: fetches the current conversion rate for the selected currencies and amount; called when "Get Latest Rate" is clicked.
- `get_historical_rate`: fetches the conversion rate for a specific past date; called when "Conversion Rate" is clicked.
- `get_rate_trend`: builds the 3-year quarterly rate history used for the trend chart; called automatically after a successful "Get Latest Rate" request. Reuses `get_historical_rate` internally rather than duplicating its API-calling logic.

### currency.py
Contains the functions that format a raw conversion rate into the text and numbers displayed in the app.

- `round_rate`: rounds a rate to 4 decimal places.
- `reverse_rate`: calculates the inverse of a conversion rate, guarding against division by zero.
- `format_output`: builds the final display sentence (rate, converted amount, inverse rate) shown under each button, following the brief's required wording.

### Other files
- README.md: The markdown file you are reading (this line is so meta)
- requirements.txt: states what packages need to be installed and their specific versions

## Citations

This program calls 3 different API endpoints from the Frankfurter app:

- Extracting the list of available currency codes (documentation: https://www.frankfurter.app/docs/#currencies) \
- Extracting the latest conversion rate for the specified currency codes (documentation: https://www.frankfurter.app/docs/#latest) \
- Extracting the historical conversion rate for the specified currency codes and a given date (documentation: https://www.frankfurter.app/docs/#historical)

Status codes can be looked up in the IETF's official HTTP Semantics standard documentation

- Go to https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes
  - Proceed to Section 15. Status Codes

AI Declaration: Claude (Anthropic) was used to help generate efficient code and markdown files. README inclusions, docstring edits and edge-case handling were the ideas of the student.