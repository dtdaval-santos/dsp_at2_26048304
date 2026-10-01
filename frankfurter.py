from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

# manual testing of endpoints
# curl -L "https://api.frankfurter.app/currencies"
# curl -L "https://api.frankfurter.app/2024-09-01?from=AUD&to=USD"
# curl -L "https://api.frankfurter.app/latest?from=AUD&to=ZZZ"
# curl -L "https://api.frankfurter.app/2023-06-01..2023-12-01?from=AUD&to=USD"

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.

    Parameters
    ----------
    None

    Returns
    -------
    list
        List of available currencies or None in case of error
    """
    url = f"{BASE_URL}/currencies"

    # declare a tuple beacuse of get_url return type
    status_code, response = get_url(url)

    # for more info on status codes, see https://www.rfc-editor.org/rfc/rfc9110.html
    if status_code == 200:
        currencies = json.loads(response)
        return list(currencies.keys())
    else:
        return None

# manual testing of endpoints
# curl -L "https://api.frankfurter.app/latest?from=AUD&to=USD"
# curl -L "https://api.frankfurter.app/latest?amount=50&from=AUD&to=USD"

def get_latest_rates(from_currency, to_currency, amount=1):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted. 
        Default is 1, but can be set to any positive float value; declared as default to avoid ZeroDivisionError for intermediate calculations
        The app.py module also has a check to ensure that the amount is a positive float before calling this function.

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """
    url = f"{BASE_URL}/latest?amount={amount}&from={from_currency}&to={to_currency}"
    status_code, response = get_url(url)

    # for more info on status codes, see https://www.rfc-editor.org/rfc/rfc9110.html
    if status_code == 200:
        data = json.loads(response)
        date = data['date']
        # testing the endpoint showed that the API returns the converted total amount
        converted_total = data['rates'][to_currency]
        # need to divide it by the original amount to get the rate
        rate = converted_total / amount
        return date, rate
    else:
        return None, None
    

def get_historical_rate(from_currency, to_currency, from_date, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    """

    
def get_rate_trend(from_currency: str, to_currency: str, years: int) -> dict:
    """
    Fetches historical rates for the past N years on a quarterly basis and returns a dictionary with dates as keys and rates as values.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    years : int
        Number of years in the past for which to fetch rates

    Returns
    -------
    dict
        Dictionary containing dates and their corresponding rates
    """