

import requests

def get_example():
   
    url = 'https://jsonplaceholder.typicode.com/posts/'
    response = requests.get(url)
    
    
    if response.status_code == 200:
        print("GET request successful!")
        
        print(response.json())
    else:
        print("Failed to retrieve data")

def post_example():
    
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 10
    }
    response = requests.post(url, json=data)
    
    # Check if the request was successful
    if response.status_code == 201:
        print("POST request successful!")
        # Print response content
        print(response.json())
    else:
        print("Failed to post data")

def main():
   
    print("Executing GET example...")
    get_example()
    #print("\nExecuting POST example...")
    #post_example()

if __name__ == "__main__":
    #main()
    pass



# ASSIGNMENTS

# 1. Modify the GET Example: Change the get_example function to fetch a list of posts instead of just one. Analyze the JSON structure and print out the titles of all posts.
print("............Assignment 1 ..........Raisa Ahmed.......")

import requests

def get_example1():

    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    
    if response.status_code == 200:
        print("GET request successful!")
        posts = response.json()  
        for i,post in enumerate(posts, start=1):
            print(f"Post {i}: Title: " , post['title'] )
            
    else:
        print("Failed to retrieve data")

def main():
    
    print("Executing GET example...")
    get_example1()
    

if __name__ == "__main__":
    main()
    





# 2. Error Handling: Add error handling to both functions to manage exceptions like connection errors or timeouts.
print("............Assignment 2 ..........Raisa Ahmed.......")

import requests

def get_example2():
    url = 'https://jsonplaceholder.typicode.com/posts/5'
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.status_code == 200:
            print("GET request successful!")
            print(response.json())
        else:
            print("Failed to retrieve data, status code:", response.status_code)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

def post_example2():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'Raisa',
        'body': 'Raisa Ahmed is being trained by Grow With Data',
        'userId': 20
    }
    
    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.status_code == 201:
            print("POST request successful!")
            print(response.json())
        else:
            print("Failed to post data, status code:", response.status_code)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

def main():
    print("Executing GET example...")
    get_example2()
    print("\nExecuting POST example...")
    post_example2()

if __name__ == "__main__":
    main()


# Advanced requests
"""
This module discuss advanced features like custom headers, user agents, and error handling.


Custom Headers and User Agents: These are used to provide additional information to the server about the request being made. For example, the 
`User-Agent` header can be used to simulate requests from different browsers.

Error Handling: The `try-except` blocks are used to catch and handle different types of exceptions that might occur during the request, such as network problems or invalid responses.
"""

import requests

def get_with_headers():
   
    url = 'https://jsonplaceholder.typicode.com/posts/20'
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        print("GET request with custom headers successful!")
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")

def post_with_authentication():
   

    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'RAISA',
        'body': 'Raisa is being trained by Grow With Data',
        'userId': 5
    }
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    auth = ('user', 'pass')  # Replace with actual username and password
    
    try:
        response = requests.post(url, json=data, headers=headers, auth=auth)
        response.raise_for_status()
        print("POST request with authentication successful!")
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")

def main():
    """
    Main function to execute advanced examples.
    """
    print("Executing GET example...")
    get_example()
    print("\nExecuting POST example...")
    post_example()

    # Advanced usages
    print("Executing GET request with custom headers...")
    get_with_headers()
    print("\nExecuting POST request with authentication...")
    post_with_authentication()

if __name__ == "__main__":
    main()
    #pass


