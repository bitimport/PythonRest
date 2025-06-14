import requests
import snowflake.connector

def consume_rest_api(url, params=None, headers=None):
    """
    Consumes a REST API using a GET request.

    :param url: The API endpoint URL.
    :param params: Dictionary of query parameters (optional).
    :param headers: Dictionary of request headers (optional).
    :return: Response JSON or None if the request fails.
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    api_url = "https://api.example.com/data"
    query_params = {"key": "value"}
    custom_headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

    result = consume_rest_api(api_url, params=query_params, headers=custom_headers)
    if result:
        print("API Response:", result)
    else:
        print("Failed to fetch data from the API. Please check your API key or access token.")




    def connect_to_snowflake(user, password, account, warehouse, database, schema):
        """
        Connects to a Snowflake database and returns the connection object.

        :param user: Snowflake username.
        :param password: Snowflake password.
        :param account: Snowflake account identifier.
        :param warehouse: Snowflake warehouse name.
        :param database: Snowflake database name.
        :param schema: Snowflake schema name.
        :return: Snowflake connection object.
        """
        try:
            conn = snowflake.connector.connect(
                user=user,
                password=password,
                account=account,
                warehouse=warehouse,
                database=database,
                schema=schema
            )
            print("Successfully connected to Snowflake.")
            return conn
        except snowflake.connector.Error as e:
            print(f"An error occurred while connecting to Snowflake: {e}")
            return None

    # Example usage
    snowflake_user = "your_username"
    snowflake_password = "your_password"
    snowflake_account = "your_account"
    snowflake_warehouse = "your_warehouse"
    snowflake_database = "your_database"
    snowflake_schema = "your_schema"

    snowflake_conn = connect_to_snowflake(
        snowflake_user,
        snowflake_password,
        snowflake_account,
        snowflake_warehouse,
        snowflake_database,
        snowflake_schema
    )

    if snowflake_conn:
        # Perform database operations here
        snowflake_conn.close()