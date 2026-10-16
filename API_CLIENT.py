"""Simple API client.

Calls the public JSONPlaceholder REST API (no API key required), reads the
JSON response and prints selected fields in a clean format.

Usage:
    python api_client.py          # shows user 1
    python api_client.py 5        # shows user 5
"""

import sys

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10  # seconds


def fetch_user(user_id: int) -> dict | None:
    """GET a single user. Returns the parsed JSON dict, or None on failure."""
    url = f"{BASE_URL}/users/{user_id}"
    try:
        response = requests.get(url, timeout=TIMEOUT)
    except requests.exceptions.Timeout:
        print("Error: the request timed out. Try again later.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: could not connect. Check your internet connection.")
        return None
    except requests.exceptions.RequestException as exc:
        print(f"Error: unexpected problem making the request: {exc}")
        return None

    # Check the HTTP status code
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Error: the server did not return valid JSON.")
            return None
    if response.status_code == 404:
        print(f"Error 404: user {user_id} was not found.")
    elif response.status_code >= 500:
        print(f"Error {response.status_code}: server problem. Try again later.")
    else:
        print(f"Error {response.status_code}: request failed.")
    return None


def display_user(user: dict) -> None:
    """Print selected fields from the user JSON in a clean format."""
    address = user.get("address", {})
    company = user.get("company", {})

    print("=" * 40)
    print(f"  User #{user.get('id')}")
    print("=" * 40)
    print(f"  Name    : {user.get('name', 'N/A')}")
    print(f"  Email   : {user.get('email', 'N/A')}")
    print(f"  Phone   : {user.get('phone', 'N/A')}")
    print(f"  City    : {address.get('city', 'N/A')}")
    print(f"  Company : {company.get('name', 'N/A')}")
    print(f"  Website : {user.get('website', 'N/A')}")
    print("=" * 40)


def main() -> None:
    try:
        user_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    except ValueError:
        print("Usage: python api_client.py [user_id]  (user_id must be a number)")
        return

    user = fetch_user(user_id)
    if user:
        display_user(user)


if __name__ == "__main__":
    main()