# Christopher Villarreal
# Module 9 Assignment 2 - APIs
# November 27, 2025
# Purpose:  Allows user to choose between two API call examples:
#           1. A tutorial API call that fetches data about astronauts currently in space.
#           2. PokeAPI will fetch data about a specified Pokémon and display it in raw or formatted JSON.

import requests, json

# Makes the JSON output more readable
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=3)
    print(text)

# Followed Tutorial from DataQuest.com
def tutorial_api_call():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(f"Status Code: {response.status_code}")

    jprint(response.json())

# PokeAPI
def poke_api_call(pokemon_name):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        
        # Check for any HTTP errors
        response.raise_for_status()

        data = response.json()

        user_choice = input("Would you like to see the output as (1) Raw or (2) Formatted? Enter 1 or 2: ")

        if user_choice == '1':
            print(f"\nDisplaying raw data for {pokemon_name.title()}:\n")
            print(data)

        elif user_choice == '2':
            print(f"\nDisplaying formatted data for {pokemon_name.title()}:\n")
            jprint(data)

    except requests.exceptions.HTTPError:
        print(f"Error: We could not find Pokemon '{pokemon_name}' Double check your spelling, or try Snorlax.")
    except Exception as error:
        print(f"An error occurred: {error}")

def main():
    # Allow user to choose which API to call
    while True:
        print("\nAPI Call Tutorial")
        print("1. Run API Call Tutorial")
        print("2. Run PokeAPI")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("Running API Call Tutorial...\n")
            tutorial_api_call()
        elif choice == '2':
            print("Running PokeAPI...\n")
            pokemon_name = input("Enter the name of the Pokémon: ").strip().lower()
            poke_api_call(pokemon_name)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()