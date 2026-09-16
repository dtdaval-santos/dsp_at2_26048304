import requests

def get_url(url: str) -> (int, str):
    """
    Function that will call a provided GET API endpoint url and return its status code and either its content or error message as a string.
    Programmed to catch exceptions in a try/except block so callers of the functions in the other modules do not need to handle exceptions downstream.

    Possible exceptions (non-exhaustive): No internet connection, DNS failure, timeout, etc.

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """

    try:
        # timeout set to 10 seconds to avoid hanging indefinitely if the API endpoint is unresponsive
        response = requests.get(url, timeout=10)
        # satisfies tuple: integer and string
        return response.status_code, response.text
    except requests.exceptions.RequestException as error:
        # satisfies values even though API did not return a response. None instead of an integer for the status code to make errors distinct.
        return None, str(error)