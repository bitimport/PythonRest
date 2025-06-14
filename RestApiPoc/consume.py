import requests

def consume_rest_api():
    # Define the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # Make a GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            print(f"Data fetched successfully:{len(data)} items found.")
            print("Response from API:")
            for item in data[:2]:  # Print the first 5 items for brevity
                print(item)
            # List number of posts for each user
            user_posts_count = {}
            for item in data:
                user_id = item['userId']
                if user_id in user_posts_count:
                    user_posts_count[user_id] += 1
                else:
                    user_posts_count[user_id] = 1
            
            # Print the count of posts for each user
            print("\nNumber of posts for each user:")
            for user_id, count in user_posts_count.items():
                print(f"User {user_id}: {count} posts")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    consume_rest_api()