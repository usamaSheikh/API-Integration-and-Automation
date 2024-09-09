import requests
import json

# API endpoint to interact with
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# Function to send a new post to the API
def send_data_to_api(title, body, user_id):
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(BASE_URL, json=data)
    
    if response.status_code == 201:
        print("Post successfully created!")
        print("Response Data:", response.json())
    else:
        print(f"Failed to create post: {response.status_code}")

# Function to retrieve data from the API
def get_data_from_api():
    response = requests.get(BASE_URL)
    
    if response.status_code == 200:
        posts = response.json()
        print(f"Successfully retrieved {len(posts)} posts.")
        # Save data locally
        with open('posts.json', 'w') as file:
            json.dump(posts, file, indent=4)
        print("Posts saved to 'posts.json'.")
    else:
        print(f"Failed to retrieve posts: {response.status_code}")

# Sample Usage
if __name__ == "__main__":
    # Sending a new post to the API
    send_data_to_api(title="Automating API Integration", body="This is a sample post to demonstrate API integration.", user_id=1)
    
    # Retrieving and saving all posts from the API
    get_data_from_api()
