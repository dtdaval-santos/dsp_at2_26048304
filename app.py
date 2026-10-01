import streamlit as st
import datetime
import pandas as pd

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate, get_rate_trend # Based on project brief screenshot chart is needed though not stated in template files
from currency import format_output, reverse_rate, round_rate # *_rate functions are used in format_output function; imported here for completeness

# Display Streamlit App Title
st.title("FX Converter")

# Get the list of available currencies from Frankfurter
currencies = get_currencies_list()

# If the list of available currencies is None, display an error message in Streamlit App
if currencies is None:
    st.error("Error: Unable to fetch the list of available currencies from source (Frankfurter). Please try again later.")
    st.stop()

# A number input where user can enter the amount to be converted
amount = st.number_input("Enter the amount to be converted:", min_value=1.0, value=1.0)

# A select box listing all the currencies available on Frankfurter
# A second select box listing all the currencies available on Frankfurter
from_currency = st.selectbox("From Currency:", options=sorted(currencies))
to_currency = st.selectbox("To Currency:", options=sorted(currencies))

# Add a button to get and display the latest rate for selected currencies and amount
if st.button("Get Latest Rate"):
    # Call the get_latest_rates function from frankfurter.py
    date, rate = get_latest_rates(from_currency, to_currency, amount)

    # Encode the positive case first
    if rate is not None:
        st.subheader("Latest Conversion Rate")
        # A text box that will display the expected text described previously
        st.write(format_output(date, from_currency, to_currency, rate, amount))

        # Based on project brief screenshot chart is needed though not stated in template files
        # Project brief screenshot showed lookback of 12 quarters (3 years)
        trend = get_rate_trend(from_currency, to_currency, years=3)

        if trend:
            st.subheader("Rate Trend Over the Last 3 years")
            trend_series = pd.Series(trend, name=f"{from_currency}/{to_currency}") # Not displayed but named for completeness on backend
            st.line_chart(trend_series)
    # A text box that will display the error encountered
    else:
        st.error(f"Unable to fetch the latest rate for {from_currency} to {to_currency}. Please try a different input or try again later.")

# Add a date selector (calendar)
# A date input where user can select a date in the past
selected_date = st.date_input("Select a date for historical rates:", max_value=datetime.date.today())

# Add a button to get and display the historical rate for selected date, currencies and amount
if st.button("Conversion Rate"):
    date_str = selected_date.strftime("%Y-%m-%d")
    # Call the get_historical_rate function from frankfurter.py and pass the parameters in the same order as defined in the function signature
    date, rate = get_historical_rate(from_currency, to_currency, date_str, amount)

    # Encode the positive case first
    if rate is not None:
        st.subheader("Historical Conversion Rate")
        # A text box that will display the expected text described previously
        st.write(format_output(date, from_currency, to_currency, rate, amount))
    # A text box that will display the error encountered; chart was only for latest rate so none here
    else:
        st.error(f"Unable to fetch the historical rate for {from_currency} to {to_currency} on {selected_date}. Please try a different input or try again later.")

# A text box that will display the expected text described previously









