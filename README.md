# What's For Dinner proxy server

The What's For Dinner is to be used with the [What's For Dinner mobile app project](https://github.com/compugrl/whats-for-dinner)

## Quick Start

1. Clone this repository. **You do not need to fork it first.**
    - `git clone https://github.com/compugrl/whats-for-dinner-back-end.git`

1. Create and activate a virtual environment
    - `python3 -m venv venv`
    - `source venv/bin/activate`
1. Install the `requirements.txt`
    - `pip install -r requirements.txt`
1. Create a `.env` file with your API keys
    ```bash
    # .env

    # Edamam API key
    RECIPE_KEY="replace_with_your_app_key"
    RECIPE_APP="replace_with_your_app_id"

    ```

1. Run the server
    - `flask run`

## Endpoints

| Route | Query Parameter(s) | Query Parameter(s) Description |
|--|--|--|
|`GET` `/recipe`| `q` | Free-form query string to search for. For `What's For Dinner`, this should be the ingredient name. |



