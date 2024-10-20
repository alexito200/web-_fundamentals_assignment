import requests
import json

# Function to fetch planet data from the Solar System OpenData API
def fetch_planet_data():
    url = 'https://api.le-systeme-solaire.net/rest/bodies/'
    response = requests.get(url)
    
    if response.status_code == 200:  # Check if the request is successful
        planets_data = json.loads(response.text)['bodies']
        
        # Filter for planets only (the API includes moons and other bodies)
        planets = [planet for planet in planets_data if planet['isPlanet']]
        
        # Initialize variables to find the heaviest planet
        heaviest_planet_name = None
        max_mass = 0

        # Extract relevant data for each planet
        for planet in planets:
            name = planet.get('englishName', 'Unknown')
            mass_value = planet.get('mass', {}).get('massValue', 0)
            mass_exponent = planet.get('mass', {}).get('massExponent', 0)
            orbital_period = planet.get('sideralOrbit', 'Unknown')  # Orbital period in days
            
            # Calculate full mass
            full_mass = mass_value * (10 ** mass_exponent)

            # Update heaviest planet information
            if full_mass > max_mass:
                max_mass = full_mass
                heaviest_planet_name = name

            # Displaying the data
            print(f"Planet: {name}")
            print(f"Mass: {full_mass:.2e} kg")  # Display in scientific notation
            print(f"Orbital Period: {orbital_period} days")
            print("-" * 30)  # Separator for readability

        # Print the heaviest planet
        if heaviest_planet_name:
            print(f"The heaviest planet is {heaviest_planet_name} with a mass of {max_mass:.2e} kg.")
    else:
        print(f"Failed to fetch data from the API. Status code: {response.status_code}")

# Fetch and display planet data
fetch_planet_data()
