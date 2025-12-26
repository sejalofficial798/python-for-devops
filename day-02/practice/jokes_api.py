import requests
import os
"""
As a devops engineer, you will have to navigate through multiple
external endpoints, and you should know how to switch them with Python
"""

pj_url = "https://official-joke-api.appspot.com/random_joke"
dad_joke_url = "https://icanhazdadjoke.com/"

def get_joke(url_type,mood):
    headers = {
        "Accept": "application/json"
    }
    joke = requests.get(url=url_type,headers=headers)
    if mood == "dad":
        
        final_joke = joke.json()["joke"]
    if mood == "pj":
        final_joke = joke.json()["setup"] + joke.json()["punchline"]
    return final_joke


mood = input("Which joke would you like to hear? eg. (Dad, PJ)")
if mood == "dad":
    url_type = dad_joke_url
elif mood == "pj":
    url_type = pj_url
else:
    url_type = dad_joke_url

final_joke = get_joke(url_type,mood)

print(final_joke)

# import requests
# import json


# api_url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url=api_url)
# data = response.json()

# first_post = data[0]

# print("Post ID:", first_post["id"])
# print("Title:", first_post["title"])
# print("Body:", first_post["body"])


# with open("output.json", "w") as file:
#     json.dump(first_post, file, indent=4)

# print("Data saved to output.json")