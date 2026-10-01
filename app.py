import streamlit as st
import datetime
import pandas as pd

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate, get_rate_trend # Based on project brief screenshot chart is needed though not stated in template files
from currency import reverse_rate, round_rate, format_output

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
        st.write(format_output(date, from_currency, to_currency, rate, amount))

        # based on project brief screenshot chart is needed though not stated in template files
        # project brief screenshot showed lookback of 12 quarters (3 years)
        trend = get_rate_trend(from_currency, to_currency, years=3)

        if trend:
            st.subheader("Rate Trend Over the Last 3 years")
            trend_series = pd.Series(trend, name=f"{from_currency}/{to_currency}") # Not displayed but named for completeness on backend
            st.line_chart(trend_series)
    # Error handling for the negative case
    else:
        st.error(f"Unable to fetch the latest rate for {from_currency} to {to_currency}. Please try again later.")

# Add a date selector (calendar)

# Add a button to get and display the historical rate for selected date, currencies and amount



# A text box that will display the expected text described previously
# A date input where user can select a date in the past
# A text box that will display the expected text described previously









