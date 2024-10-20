import requests
import json

# Function to fetch Pokémon data
def fetch_pokemon_data(pokemon_names):
    pokemon_data_list = []
    
    for name in pokemon_names:  # Iterate over the list of Pokémon names
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        response = requests.get(url)
        
        if response.status_code == 200:  # Check if the request is successful
            json_data = response.text
            pokemon_data = json.loads(json_data)
            
            # Add the Pokémon's data to the list
            pokemon_data_list.append(pokemon_data)
            
            # Print details for each Pokémon
            print(f"Pokemon: {pokemon_data['name']}")
            print(f"Height: {pokemon_data['height']}")
            print(f"Weight: {pokemon_data['weight']}")
            print("-" * 30)  # Separator for readability
        else:
            print(f"Failed to fetch data for {name}")
    
    return pokemon_data_list

# Function to calculate the average weight
def calculate_average_weight(pokemon_data_list):
    total_weight = 0
    count = len(pokemon_data_list)
    
    for pokemon_data in pokemon_data_list:
        total_weight += pokemon_data['weight']  # Sum the weights
    
    # Calculate and return the average weight
    if count > 0:
        return total_weight / count
    else:
        return 0  # Return 0 if no data is available

# List of Pokémon names
pokemon_names = ['pikachu', 'bulbasaur', 'charmander']

# Fetch Pokémon data
pokemon_data_list = fetch_pokemon_data(pokemon_names)

# Calculate and print the average weight
average_weight = calculate_average_weight(pokemon_data_list)
print(f"Average weight of the Pokémon: {average_weight}")
