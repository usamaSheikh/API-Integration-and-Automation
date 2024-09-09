# API-Integration-and-Automation
API Integration and Automation, where you can automate sending data to a third-party API, retrieving information, and syncing it between systems. In this example, we’ll integrate with a mock REST API to demonstrate how to send data, retrieve responses, and store the data in a local file.

### Technologies Used:
- Python
- `requests` library

### API Used:
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/), a free fake online REST API.

## How to Run the Script:
1. Clone this repository.
2. Install the required package:
    ```bash
    pip install requests
    ```
3. Run the script:
    ```bash
    python api_integration.py
    ```
4. The script will send a sample post to the API and retrieve all posts, saving them in a file called `posts.json`.

### Example Output:
- A new post will be created and confirmed in the console.
- All posts will be saved to a local file (`posts.json`).

## Screenshots:
![image](https://github.com/user-attachments/assets/e8d1d42a-327f-44f3-a548-d9a1f25e8915)

![image](https://github.com/user-attachments/assets/b1883cac-5777-45f4-b49b-af67fa0042c9)

![image](https://github.com/user-attachments/assets/e29ad0de-638d-4f16-9315-e55d0197b855)


