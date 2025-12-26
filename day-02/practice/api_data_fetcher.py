import requests
import json

# Function to fetch joke from API

def fetch_joke():
    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    response = requests.get(url)
    return response.json()


#  process joke data

def process_joke(joke_data):
    joke = joke_data[0]   

    processed_joke = {
        "id": joke["id"],
        "type": joke["type"],
        "setup": joke["setup"],
        "punchline": joke["punchline"]
    }

    return processed_joke

# save joke to JSON file

def save_to_json(data, filename="output.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# Main function

def main():
    print("Fetching a programming joke from API...\n")

    joke_data = fetch_joke()
    joke = process_joke(joke_data)

    print("Setup:", joke["setup"])
    print("Punchline:", joke["punchline"])

    save_to_json(joke)
    print("\nJoke saved to output.json")


# Run only when executed directly
if __name__ == "__main__":
    main()
