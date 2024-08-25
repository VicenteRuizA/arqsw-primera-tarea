import requests
import logging

async def add(counter, amount):
    base_url = 'http://ms-to:8090/add'
    headers = {'Content-Type': 'application/json'}
    timeout = 10

    body_parameters = {
            "counter": counter,
            "amount": amount
            }
    try:
        response = requests.post(base_url, headers=headers, json=body_parameters, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        logging.error("The request timed out")
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    return None
